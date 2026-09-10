"""
Clase Comedor que implementa composición.
Un comedor está compuesto por una mesa y varias sillas.
"""

from typing import List
from ..concretos.mesa import Mesa
from ..concretos.silla import Silla


class Comedor:
    """
    Clase que implementa composición conteniendo una mesa y sillas.
    
    Un comedor es un conjunto de muebles que trabajan juntos.
    La relación es de composición porque el comedor "tiene" una mesa
    y "tiene" sillas, pero estas pueden existir independientemente.
    
    Conceptos OOP aplicados:
    - Composición: El comedor contiene otros objetos (mesa y sillas)
    - Agregación: Los objetos contenidos pueden existir independientemente
    - Encapsulación: Controla el acceso a los componentes internos
    - Abstracción: Simplifica la gestión de múltiples muebles
    """
    
    def __init__(self, nombre: str, mesa: 'Mesa', sillas: List['Silla'] = None):
        """
        Constructor del comedor.
        
        Args:
            nombre: Nombre del set de comedor
            mesa: Objeto Mesa que forma parte del comedor
            sillas: Lista de objetos Silla (opcional, se puede crear vacía)
        """
        if not isinstance(mesa, Mesa):
            raise TypeError("El comedor debe tener una mesa válida")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre.strip()
        self._mesa = mesa
        self._sillas = []
        for silla in sillas or []:
            if not isinstance(silla, Silla):
                raise TypeError("Solo se pueden agregar objetos de tipo Silla")
            self._sillas.append(silla)
    
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def mesa(self) -> 'Mesa':
        return self._mesa

    @property
    def sillas(self) -> List['Silla']:
        return self._sillas.copy()
    
    def agregar_silla(self, silla: 'Silla') -> str:
        """
        Agrega una silla al comedor.
        
        Args:
            silla: Objeto Silla a agregar
            
        Returns:
            str: Mensaje de confirmación
        """
        if not isinstance(silla, Silla):
            return "Error: Solo se pueden agregar objetos de tipo Silla"
        if len(self._sillas) >= self._calcular_capacidad_maxima():
            return (f"No se pueden agregar más sillas. Capacidad máxima: "
                    f"{self._calcular_capacidad_maxima()}")
        self._sillas.append(silla)
        return f"Silla {silla.nombre} agregada exitosamente al comedor"
    
    def quitar_silla(self, indice: int = -1) -> str:
        """
        Quita una silla del comedor.
        
        Args:
            indice: Índice de la silla a quitar (-1 para la última)
            
        Returns:
            str: Mensaje de confirmación
        """
        if not self._sillas:
            return "No hay sillas para quitar"
        try:
            silla_removida = self._sillas.pop(indice)
        except IndexError:
            return "Índice de silla inválido"
        return f"Silla {silla_removida.nombre} removida del comedor"
    
    def calcular_precio_total(self) -> float:
        """
        Calcula el precio total del comedor sumando todos sus componentes.
        
        Returns:
            float: Precio total del set de comedor
        """
        precio_total = self._mesa.calcular_precio() + sum(
            silla.calcular_precio() for silla in self._sillas)
        if len(self._sillas) >= 4:
            precio_total *= 0.95
        return round(precio_total, 2)
    
    def obtener_descripcion_completa(self) -> str:
        """
        Obtiene una descripción completa del comedor y todos sus componentes.
        
        Returns:
            str: Descripción detallada del comedor
        """
        descripcion = f"=== COMEDOR {self.nombre.upper()} ===\n\nMESA:\n"
        descripcion += self._mesa.obtener_descripcion() + "\n\n"
        if self._sillas:
            descripcion += f"SILLAS ({len(self._sillas)} unidades):\n"
            for i, silla in enumerate(self._sillas, 1):
                descripcion += f"{i}. {silla.obtener_descripcion()}\n"
        else:
            descripcion += "SILLAS: Ninguna incluida\n"
        descripcion += f"\n--- PRECIO TOTAL: ${self.calcular_precio_total():.2f} ---"
        if len(self._sillas) >= 4:
            descripcion += "\n(Incluye 5% de descuento por set completo)"
        return descripcion
    
    def _calcular_capacidad_maxima(self) -> int:
        """
        Calcula la capacidad máxima de sillas basada en el tamaño de la mesa.
        Método privado auxiliar.
        
        Returns:
            int: Número máximo de sillas que pueden acomodarse
        """
        return getattr(self._mesa, "capacidad_personas", 6)
    
    def obtener_resumen(self) -> dict:
        """
        Obtiene un resumen estadístico del comedor.
        
        Returns:
            dict: Diccionario con información resumida
        """
        return {
            "nombre": self.nombre,
            "total_muebles": len(self),
            "precio_mesa": self._mesa.calcular_precio(),
            "precio_sillas": sum(silla.calcular_precio() for silla in self._sillas),
            "precio_total": self.calcular_precio_total(),
            "capacidad_personas": len(self._sillas),
            "materiales_utilizados": self._obtener_materiales_unicos(),
        }
    
    def _obtener_materiales_unicos(self) -> list:
        """
        Obtiene una lista de materiales únicos usados en el comedor.
        Método privado auxiliar.
        
        Returns:
            list: Lista de materiales únicos
        """
        materiales = {self._mesa.material}
        for silla in self._sillas:
            materiales.add(silla.material)
            if silla.material_tapizado:
                materiales.add(silla.material_tapizado)
        return sorted(materiales)
    
    def __str__(self) -> str:
        """Representación en cadena del comedor."""
        return f"Comedor {self.nombre}: Mesa + {len(self._sillas)} sillas"
    
    def __len__(self) -> int:
        """Retorna el número total de muebles en el comedor."""
        return 1 + len(self._sillas)

