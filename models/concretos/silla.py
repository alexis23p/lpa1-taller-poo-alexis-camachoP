"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

from ..categorias.asientos import Asiento


class Silla(Asiento):
    """
    Clase concreta que representa una silla.
    
    Una silla es un asiento individual con características específicas
    como altura regulable, ruedas, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la silla
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        """
        Constructor de la silla.
        
        Args:
            altura_regulable: Si la silla puede regular su altura
            tiene_ruedas: Si la silla tiene ruedas
            Otros argumentos heredados de Asiento
        """
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)
        self.altura_regulable = altura_regulable
        self.tiene_ruedas = tiene_ruedas
    
    @property
    def altura_regulable(self) -> bool:
        return self._altura_regulable

    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        self._altura_regulable = bool(value)

    @property
    def tiene_ruedas(self) -> bool:
        return self._tiene_ruedas

    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        self._tiene_ruedas = bool(value)
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sillas.
        
        Returns:
            float: Precio final de la silla
        """
        precio = self.precio_base * self.calcular_factor_comodidad()
        if self.altura_regulable:
            precio += 75
        if self.tiene_ruedas:
            precio += 50
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la silla.
        
        Returns:
            str: Descripción completa de la silla
        """
        descripcion = f"Silla {self.nombre} de {self.material}, color {self.color}."
        descripcion += f"\n{self.obtener_info_asiento()}"
        descripcion += f"\nAltura regulable: {'Sí' if self.altura_regulable else 'No'}"
        descripcion += f", Ruedas: {'Sí' if self.tiene_ruedas else 'No'}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion
    
    def regular_altura(self, nueva_altura: int) -> str:
        """
        Simula la regulación de altura de la silla.
        Método específico de la clase Silla.
        
        Args:
            nueva_altura: Nueva altura en centímetros
            
        Returns:
            str: Mensaje del resultado de la operación
        """
        if not self.altura_regulable:
            return "Esta silla no tiene mecanismo de regulación de altura"
        if not isinstance(nueva_altura, (int, float)) or not 30 <= nueva_altura <= 60:
            return "La altura debe estar entre 30 y 60 centímetros"
        return f"Altura regulada a {nueva_altura} cm"
    
    def es_silla_oficina(self) -> bool:
        """
        Determina si la silla es adecuada para oficina.
        
        Returns:
            bool: True si es silla de oficina
        """
        return self.tiene_ruedas and self.altura_regulable

