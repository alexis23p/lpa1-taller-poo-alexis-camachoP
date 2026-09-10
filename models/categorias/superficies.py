"""
Clase abstracta para muebles para superficies de trabajo o del hogar.
Esta clase agrupa características comunes de mesas, escritorios, etc.
"""

from abc import abstractmethod
from ..mueble import Mueble


class Superficie(Mueble):
    """
    Clase abstracta para todos los muebles que proporcionan superficies de trabajo.
    
    Hereda de Mueble y añade características específicas de muebles con superficies
    como forma, dimensiones, capacidad, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de superficies
    - Polimorfismo: Permite diferentes implementaciones del cálculo de estabilidad
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str = "rectangular", capacidad_personas: int = 4):
        """
        Constructor para muebles con superficie.
        
        Args:
            nombre: Nombre del mueble
            material: Material del mueble
            color: Color del mueble
            precio_base: Precio base del mueble
            forma: Forma de la superficie (rectangular, redonda, L, etc.)
            capacidad_personas: Número de personas que puede soportar
        """
        super().__init__(nombre, material, color, precio_base)
        self.forma = forma
        self.capacidad_personas = capacidad_personas
    
    @property
    def forma(self) -> str:
        return self._forma

    @forma.setter
    def forma(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("La forma no puede estar vacía")
        self._forma = value.strip()

    @property
    def capacidad_personas(self) -> int:
        return self._capacidad_personas

    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._capacidad_personas = value
    
    def calcular_factor_estabilidad(self) -> float:
        """
        Calcula un factor de estabilidad basado en las características de la superficie.
        Método concreto que pueden usar las clases hijas.
        
        Returns:
            float: Factor multiplicador de estabilidad (1.0 = neutral)
        """
        factor = 1.0
        
        # Formas más estables tienen mejor factor
        forma_lower = self.forma.lower()
        if forma_lower == "rectangular":
            factor = 1.0
        elif forma_lower == "redonda":
            factor = 0.95  # Más elegante pero ligeramente menos estable
        elif forma_lower == "l" or forma_lower == "esquina":
            factor = 1.05  # Más funcional
        
        # Capacidad influye en la estabilidad
        factor += (self.capacidad_personas - 1) * 0.05
        
        return factor
    
    def obtener_info_superficie(self) -> str:
        """
        Obtiene información específica de la superficie.
        Método concreto auxiliar para las clases hijas.
        
        Returns:
            str: Información detallada de la superficie
        """
        return f"Forma: {self.forma}, Capacidad: {self.capacidad_personas} personas"
    
    @abstractmethod
    def calcular_precio(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def obtener_descripcion(self) -> str:
        raise NotImplementedError
