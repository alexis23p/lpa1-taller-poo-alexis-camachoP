"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

from .sofa import Sofa
from .cama import Cama


class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.
    
    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.
    
    Conceptos OOP aplicados:
    - Herencia múltiple: Hereda de Sofa y Cama
    - Resolución MRO: Maneja el orden de resolución de métodos
    - Polimorfismo: Implementa comportamientos únicos combinando funcionalidades
    - Super(): Usa super() para resolver conflictos de herencia
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, material_tapizado: str = "tela",
                 tamaño_cama: str = "matrimonial", incluye_colchon: bool = True,
                 mecanismo_conversion: str = "plegable"):
        """
        Constructor del sofá-cama.
        
        Args:
            mecanismo_conversion: Tipo de mecanismo de conversión (plegable, extensible, etc.)
            Otros argumentos se pasan a las clases padre
        """
        Sofa.__init__(self, nombre, material, color, precio_base, capacidad_personas,
                  True, material_tapizado)
        self._tamaño_cama = tamaño_cama
        self._incluye_colchon = bool(incluye_colchon)
        self._mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"
    
    @property
    def tamaño_cama(self):
        return self._tamaño_cama

    @property
    def incluye_colchon(self):
        return self._incluye_colchon

    @property
    def mecanismo_conversion(self) -> str:
        return self._mecanismo_conversion

    @property
    def modo_actual(self) -> str:
        return self._modo_actual
    
    def convertir_a_cama(self) -> str:
        """
        Convierte el sofá en cama.
        Método específico del sofá-cama.
        
        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "cama":
            return "El sofá-cama ya está en modo cama"
        self._modo_actual = "cama"
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"
    
    def convertir_a_sofa(self) -> str:
        """
        Convierte la cama en sofá.
        Método específico del sofá-cama.
        
        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "sofa":
            return "El sofá-cama ya está en modo sofá"
        self._modo_actual = "sofa"
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
    
    def calcular_precio(self) -> float:
        """
        Calcula el precio combinando las funcionalidades de sofá y cama.
        
        Returns:
            float: Precio final del sofá-cama
        """
        precio = self.precio_base * self.calcular_factor_comodidad() * 1.5
        precio += {"electrico": 200, "hidraulico": 150}.get(
            self.mecanismo_conversion, 100)
        if self.incluye_colchon:
            precio += 300
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Descripción que combina características de sofá y cama.
        
        Returns:
            str: Descripción completa del sofá-cama
        """
        return (f"Sofá-cama {self.nombre} fabricado en {self.material} color {self.color}.\n"
            f"{self.obtener_info_asiento()}\nTamaño de cama: {self.tamaño_cama}\n"
            f"Mecanismo de conversión: {self.mecanismo_conversion}\n"
            f"Colchón incluido: {'Sí' if self.incluye_colchon else 'No'}\n"
            f"Modo actual: {self.modo_actual}\nPrecio: ${self.calcular_precio():.2f}")
    
    def obtener_capacidad_total(self) -> dict:
        """
        Obtiene la capacidad tanto como sofá como cama.
        Método único del sofá-cama.
        
        Returns:
            dict: Capacidades en ambos modos
        """
        return {"como_sofa": self.capacidad_personas,
            "como_cama": 2 if self.tamaño_cama in ["matrimonial", "queen", "king"] else 1}
    
    def puede_usar_como_cama(self):
        return self._modo_actual == "cama"

    def puede_usar_como_sofa(self):
        return self._modo_actual == "sofa"
    
    def __str__(self) -> str:
        """
        Representación en cadena del sofá-cama.
        Sobrescribe el método heredado para mostrar información específica.
        """
        return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"

