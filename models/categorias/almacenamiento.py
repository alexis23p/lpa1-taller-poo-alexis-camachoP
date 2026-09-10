"""
Clase abstracta para muebles de almacenamiento.
Esta clase agrupa características comunes de armarios, cajoneras, etc.
"""

from abc import abstractmethod
from ..mueble import Mueble


class Almacenamiento(Mueble):
    """
    Clase abstracta para todos los muebles de almacenamiento.
    
    Hereda de Mueble y añade características específicas de almacenamiento
    como número de puertas, cajones, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de almacenamiento
    - Polimorfismo: Permite diferentes implementaciones del cálculo de capacidad
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 num_espacios: int = 1):
        """
        Constructor para muebles de almacenamiento.
        
        Args:
            nombre: Nombre del mueble
            material: Material del mueble
            color: Color del mueble
            precio_base: Precio base del mueble
            num_espacios: Número de espacios de almacenamiento (puertas, cajones, etc.)
        """
        super().__init__(nombre, material, color, precio_base)
        self.num_espacios = num_espacios
    
    @property
    def num_espacios(self) -> int:
        return self._num_espacios

    @num_espacios.setter
    def num_espacios(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El número de espacios debe ser mayor a 0")
        self._num_espacios = value
    
    def calcular_capacidad(self) -> float:
        """
        Calcula la capacidad de almacenamiento del mueble.
        Método concreto que puede ser usado por las clases hijas.
        
        Returns:
            float: Capacidad en unidades relativas
        """
        return self.num_espacios * 10.0
    
    def obtener_info_almacenamiento(self) -> str:
        """
        Obtiene información específica del almacenamiento.
        Método concreto auxiliar para las clases hijas.
        
        Returns:
            str: Información detallada del almacenamiento
        """
        return f"Espacios de almacenamiento: {self.num_espacios}, Capacidad: {self.calcular_capacidad()}"
    
    @abstractmethod
    def calcular_precio(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def obtener_descripcion(self) -> str:
        raise NotImplementedError
