"""
Clase abstracta para muebles de asiento.
Esta clase agrupa las características comunes de sillas, sillones y sofás.
"""

from abc import abstractmethod
from ..mueble import Mueble


class Asiento(Mueble):
    """
    Clase abstracta para todos los muebles donde las personas se sientan.
    
    Hereda de Mueble y añade características específicas de los asientos
    como capacidad de personas, tipo de respaldo, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de asientos
    - Polimorfismo: Permite diferentes implementaciones del cálculo de comodidad
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool, material_tapizado: str = None):
        """
        Constructor para muebles de asiento.
        
        Args:
            capacidad_personas: Número de personas que pueden sentarse
            tiene_respaldo: Si el asiento tiene respaldo o no
            material_tapizado: Material del tapizado (opcional)
            Otros argumentos heredados de Mueble
        """
        Mueble.__init__(self, nombre, material, color, precio_base)
        self.capacidad_personas = capacidad_personas
        self.tiene_respaldo = tiene_respaldo
        self.material_tapizado = material_tapizado
    
    @property
    def capacidad_personas(self) -> int:
        return self._capacidad_personas

    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._capacidad_personas = value

    @property
    def tiene_respaldo(self) -> bool:
        return self._tiene_respaldo

    @tiene_respaldo.setter
    def tiene_respaldo(self, value: bool) -> None:
        self._tiene_respaldo = bool(value)

    @property
    def material_tapizado(self) -> str:
        return self._material_tapizado

    @material_tapizado.setter
    def material_tapizado(self, value: str) -> None:
        self._material_tapizado = value.strip() if isinstance(value, str) else value
    
    def calcular_factor_comodidad(self) -> float:
        """
        Calcula un factor de comodidad basado en las características del asiento.
        Este es un método concreto que pueden usar las clases hijas.
        
        Returns:
            float: Factor multiplicador para el precio (1.0 = neutral)
        """
        # Considerar factores como:
        # - Si tiene respaldo (+0.1)
        # - Material del tapizado (cuero +0.2, tela +0.1)
        # - Capacidad de personas (más personas = más cómodo)
        
        factor = 1.0
        
        if self.tiene_respaldo:
            factor += 0.1
        if self.material_tapizado:
            tapizado = self.material_tapizado.lower()
            if tapizado == "cuero":
                factor += 0.2
            elif tapizado == "tela":
                factor += 0.1
        
        return factor
    
    def obtener_info_asiento(self) -> str:
        """
        Obtiene información específica del asiento.
        Método concreto auxiliar para las clases hijas.
        
        Returns:
            str: Información detallada del asiento
        """
        info = f"Capacidad: {self.capacidad_personas} personas"
        info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        if self.material_tapizado:
            info += f", Tapizado: {self.material_tapizado}"
        return info
    
    @abstractmethod
    def calcular_precio(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def obtener_descripcion(self) -> str:
        raise NotImplementedError

