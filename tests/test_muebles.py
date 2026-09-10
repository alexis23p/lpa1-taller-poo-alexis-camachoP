"""
Pruebas unitarias para las clases de muebles.
Estas pruebas validan el correcto funcionamiento de todos los conceptos OOP implementados.
"""

import pytest
from models.mueble import Mueble
from models.categorias.asientos import Asiento
from models.concretos.silla import Silla
from models.concretos.sillon import Sillon
from models.concretos.sofa import Sofa
from models.concretos.sofacama import SofaCama
from models.concretos.mesa import Mesa
from models.concretos.escritorio import Escritorio
from models.concretos.armario import Armario
from models.concretos.cajonera import Cajonera
from models.concretos.cama import Cama
from models.composicion.comedor import Comedor
from services.tienda import TiendaMuebles
from services.catalogo import Catalogo


class TestMuebleBase:
    """
    Pruebas para la clase base abstracta Mueble.
    Valida conceptos de abstracción y encapsulación.
    """
    
    def test_no_puede_instanciar_mueble_directamente(self):
        """
        Prueba que no se puede instanciar la clase abstracta Mueble directamente.
        Valida el concepto de abstracción.
        """
        with pytest.raises(TypeError):
            mueble = Mueble("Test", "Madera", "Café", 100.0)
    
    def test_propiedades_mueble(self):
        """Prueba las propiedades básicas de un mueble concreto."""
        silla = Silla("Test Silla", "Madera", "Roble", 150.0)
        assert silla.nombre == "Test Silla"
        assert silla.material == "Madera"
        assert silla.color == "Roble"
        assert silla.precio_base == 150.0


class TestSilla:
    """
    Pruebas para la clase Silla.
    Valida herencia, polimorfismo y encapsulación.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.silla_basica = Silla(
            nombre="Silla Básica",
            material="Madera",
            color="Café",
            precio_base=150.0,
            tiene_respaldo=True
        )

        self.silla_oficina = Silla(
            nombre="Silla Oficina",
            material="Metal",
            color="Negro",
            precio_base=300.0,
            tiene_respaldo=True,
            material_tapizado="cuero",
            altura_regulable=True,
            tiene_ruedas=True
        )
    
    def test_creacion_silla_basica(self):
        """Prueba la creación correcta de una silla básica."""
        assert self.silla_basica.nombre == "Silla Básica"
        assert self.silla_basica.material == "Madera"
        assert self.silla_basica.tiene_respaldo == True
    
    def test_calculo_precio_silla_basica(self):
        """Prueba el cálculo de precio para silla básica."""
        precio = self.silla_basica.calcular_precio()
        assert precio == 165.0
    
    def test_calculo_precio_silla_oficina(self):
        """Prueba el cálculo de precio para silla de oficina con todas las características."""
        precio = self.silla_oficina.calcular_precio()
        assert precio == 515.0
    
    def test_es_silla_oficina(self):
        """Prueba la lógica de identificación de silla de oficina."""
        assert self.silla_oficina.es_silla_oficina() == True
        assert self.silla_basica.es_silla_oficina() == False
    
    def test_regular_altura_silla_sin_mecanismo(self):
        """Prueba que las sillas sin altura regulable no pueden ajustarse."""
        resultado = self.silla_basica.regular_altura(45)
        assert "no tiene mecanismo" in resultado.lower()
    
    def test_regular_altura_silla_con_mecanismo(self):
        """Prueba la regulación de altura en sillas que lo permiten."""
        resultado = self.silla_oficina.regular_altura(45)
        assert "regulada a 45 cm" in resultado
    
    def test_validaciones_setter(self):
        """Prueba las validaciones en los setters."""
        with pytest.raises(ValueError):
            self.silla_basica.nombre = ""

        with pytest.raises(ValueError):
            self.silla_basica.precio_base = -100
        
        with pytest.raises(ValueError):
            self.silla_basica.capacidad_personas = 0
    
    def test_obtener_descripcion(self):
        """Prueba que la descripción contenga información relevante."""
        descripcion = self.silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
        assert "Madera" in descripcion
        assert "165.00" in descripcion
    
    def test_polimorfismo_herencia(self):
        """Prueba que la silla implementa correctamente los métodos abstractos."""
        assert isinstance(self.silla_basica, Asiento)
        assert hasattr(self.silla_basica, 'calcular_precio')
        assert hasattr(self.silla_basica, 'obtener_descripcion')

        precio = self.silla_basica.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

        descripcion = self.silla_basica.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


class TestSillon:
    """Pruebas para la clase Sillón."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.sillon = Sillon(
            nombre="Sillón Reclinable",
            material="Cuero",
            color="Marrón",
            precio_base=800.0,
            tiene_respaldo=True,
            material_tapizado="cuero",
            es_reclinable=True,
            tiene_reposapiés=True
        )
    
    def test_calculo_precio_sillon(self):
        """Prueba el cálculo de precio del sillón."""
        precio = self.sillon.calcular_precio()
        # Precio base: 800.0
        # Factor comodidad: 1.3 (respaldo + cuero) = 800 * 1.3 = 1040
        # Reclinable: +250
        # Reposapiés: +100
        # Total: 1040 + 250 + 100 = 1390
        assert precio == 1390.0


class TestSofa:
    """Pruebas para la clase Sofá."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.sofa = Sofa(
            nombre="Sofá Modular",
            material="Tela",
            color="Gris",
            precio_base=1200.0,
            capacidad_personas=3,
            tiene_respaldo=True,
            material_tapizado="tela",
            es_modular=True,
            incluye_cojines=True
        )
    
    def test_calculo_precio_sofa(self):
        """Prueba el cálculo de precio del sofá."""
        precio = self.sofa.calcular_precio()
        # Precio base: 1200.0
        # Factor comodidad: 1.2 (respaldo + tela) = 1200 * 1.2 = 1440
        # Modular: +200
        # Cojines: +100
        # Total: 1440 + 200 + 100 = 1740
        assert precio == 1740.0


class TestSofaCama:
    """
    Pruebas para la clase SofaCama.
    Valida herencia múltiple y resolución MRO.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.sofacama = SofaCama(
            nombre="SofaCama Deluxe",
            material="Tela",
            color="Gris",
            precio_base=1000.0,
            capacidad_personas=3,
            tamaño_cama="matrimonial",
            incluye_colchon=True,
            mecanismo_conversion="plegable"
        )
    
    def test_creacion_sofacama(self):
        """Prueba la creación correcta del sofá-cama."""
        assert self.sofacama.nombre == "SofaCama Deluxe"
        assert self.sofacama.capacidad_personas == 3
        assert self.sofacama.tamaño_cama == "matrimonial"
        assert self.sofacama.incluye_colchon == True
        assert self.sofacama.modo_actual == "sofa"
    
    def test_conversion_modos(self):
        """Prueba la conversión entre modos sofá y cama."""
        assert self.sofacama.modo_actual == "sofa"
        resultado = self.sofacama.convertir_a_cama()
        assert "convertido a cama" in resultado.lower()
        assert self.sofacama.modo_actual == "cama"
    
    def test_capacidad_total(self):
        """Prueba las capacidades en ambos modos."""
        capacidades = self.sofacama.obtener_capacidad_total()
        assert capacidades["como_sofa"] == 3
        assert capacidades["como_cama"] == 2
    
    def test_herencia_multiple_mro(self):
        """Prueba que la herencia múltiple funciona correctamente."""
        assert isinstance(self.sofacama, Sofa)
        assert isinstance(self.sofacama, Cama)


class TestMesa:
    """Pruebas para la clase Mesa."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.mesa = Mesa(
            nombre="Mesa Comedor",
            material="Madera",
            color="Roble",
            precio_base=500.0,
            forma="rectangular",
            capacidad_personas=6
        )
    
    def test_creacion_mesa(self):
        """Prueba la creación de una mesa."""
        assert self.mesa.nombre == "Mesa Comedor"
        assert self.mesa.forma == "rectangular"
        assert self.mesa.capacidad_personas == 6


class TestArmario:
    """Pruebas para la clase Armario."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.armario = Armario(
            nombre="Armario Ropero",
            material="Madera",
            color="Blanco",
            precio_base=600.0,
            num_puertas=4,
            num_cajones=2,
            tiene_espejos=True
        )
    
    def test_calculo_precio_armario(self):
        """Prueba el cálculo de precio del armario."""
        precio = self.armario.calcular_precio()
        assert precio == 1130.0


class TestComedor:
    """
    Pruebas para la clase Comedor.
    Valida composición y agregación.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.mesa = Mesa(
            nombre="Mesa Familiar",
            material="Madera",
            color="Roble",
            precio_base=500.0,
            forma="rectangular",
            capacidad_personas=6
        )

        self.silla1 = Silla("Silla 1", "Madera", "Roble", 120.0, True)
        self.silla2 = Silla("Silla 2", "Madera", "Roble", 120.0, True)

        self.comedor = Comedor(
            nombre="Comedor Familiar",
            mesa=self.mesa,
            sillas=[self.silla1, self.silla2]
        )
    
    def test_creacion_comedor(self):
        """Prueba la creación correcta del comedor con composición."""
        assert self.comedor.nombre == "Comedor Familiar"
        assert self.comedor.mesa == self.mesa
        assert len(self.comedor.sillas) == 2
    
    def test_agregar_silla(self):
        """Prueba agregar sillas al comedor."""
        silla_nueva = Silla("Silla Nueva", "Madera", "Roble", 120.0, True)
        resultado = self.comedor.agregar_silla(silla_nueva)
        assert "exitosamente" in resultado.lower()
        assert len(self.comedor.sillas) == 3
    
    def test_len_comedor(self):
        """Prueba el método __len__ del comedor."""
        assert len(self.comedor) == 3  # Mesa + 2 sillas


class TestTiendaMuebles:
    """Pruebas para la clase TiendaMuebles."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.tienda = TiendaMuebles("Tienda Test")
        self.silla = Silla("Silla Test", "Madera", "Café", 150.0)
        self.mesa = Mesa("Mesa Test", "Madera", "Roble", 500.0)
    
    def test_agregar_mueble(self):
        """Prueba agregar muebles a la tienda."""
        resultado = self.tienda.agregar_mueble(self.silla)
        assert "exitosamente" in resultado.lower()
        assert self.tienda.total_muebles == 1
    
    def test_buscar_por_nombre(self):
        """Prueba la búsqueda de muebles por nombre."""
        self.tienda.agregar_mueble(self.silla)
        self.tienda.agregar_mueble(self.mesa)
        resultados = self.tienda.buscar_muebles_por_nombre("Silla")
        assert len(resultados) == 1
    
    def test_filtrar_por_material(self):
        """Prueba el filtrado por material."""
        self.tienda.agregar_mueble(self.silla)
        self.tienda.agregar_mueble(self.mesa)
        resultados = self.tienda.filtrar_por_material("Madera")
        assert len(resultados) == 2


class TestCatalogo:
    """Pruebas para la clase Catálogo."""
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.catalogo = Catalogo()
        self.silla = Silla("Silla Test", "Madera", "Café", 150.0)
        self.mesa = Mesa("Mesa Test", "Madera", "Roble", 500.0)
        self.catalogo.agregar_mueble(self.silla)
        self.catalogo.agregar_mueble(self.mesa)
    
    def test_busqueda_por_nombre(self):
        """Prueba la búsqueda por nombre."""
        resultados = self.catalogo.buscar_por_nombre("Silla")
        assert len(resultados) == 1
    
    def test_obtener_estadisticas(self):
        """Prueba las estadísticas del catálogo."""
        stats = self.catalogo.obtener_estadisticas()
        assert stats["total_muebles"] == 2


class TestConceptosOOPGenerales:
    """Pruebas que validan conceptos generales de OOP aplicados."""
    
    def test_polimorfismo_general(self):
        """Prueba que diferentes tipos de muebles implementan polimorfismo."""
        muebles = [
            Silla("Silla", "Madera", "Café", 100.0),
            Mesa("Mesa", "Madera", "Roble", 300.0),
        ]
        
        for mueble in muebles:
            precio = mueble.calcular_precio()
            assert isinstance(precio, (int, float)) and precio > 0
    
    def test_herencia_jerarquia(self):
        """Prueba que la jerarquía de herencia funciona correctamente."""
        silla = Silla("Silla", "Madera", "Café", 100.0)
        assert isinstance(silla, Mueble)
        assert isinstance(silla, Asiento)
