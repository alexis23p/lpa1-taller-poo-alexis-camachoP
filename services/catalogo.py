"""
Servicio de catálogo que maneja búsquedas y filtros de muebles.
"""

from typing import List, Dict, Optional
from models.mueble import Mueble


class Catalogo:
    """
    Clase que maneja la búsqueda y organización del catálogo de muebles.
    
    Proporciona funcionalidades para:
    - Búsquedas avanzadas
    - Filtros por múltiples criterios
    - Ordenamiento
    - Estadísticas del catálogo
    
    Conceptos OOP aplicados:
    - Encapsulación: Agrupa funcionalidades de búsqueda
    - Abstracción: Simplifica las búsquedas complejas
    - Composición: Trabaja con una lista de muebles
    """
    
    def __init__(self, muebles: List['Mueble'] = None):
        """
        Constructor del catálogo.
        
        Args:
            muebles: Lista inicial de muebles (opcional)
        """
        self._muebles = muebles if muebles else []
    
    def agregar_mueble(self, mueble: 'Mueble') -> bool:
        """
        Agrega un mueble al catálogo.
        
        Args:
            mueble: Mueble a agregar
            
        Returns:
            bool: True si se agregó exitosamente
        """
        if isinstance(mueble, Mueble) and mueble not in self._muebles:
            self._muebles.append(mueble)
            return True
        return False
    
    def buscar_por_nombre(self, nombre: str) -> List['Mueble']:
        """
        Busca muebles por nombre (búsqueda parcial, case-insensitive).
        
        Args:
            nombre: Nombre o parte del nombre a buscar
            
        Returns:
            List[Mueble]: Lista de muebles coincidentes
        """
        if not nombre or not nombre.strip():
            return []
        termino = nombre.lower().strip()
        return [m for m in self._muebles if termino in m.nombre.lower()]
    
    def buscar_por_tipo(self, tipo_clase) -> List['Mueble']:
        """
        Busca muebles por tipo de clase.
        
        Args:
            tipo_clase: Clase del tipo de mueble
            
        Returns:
            List[Mueble]: Lista de muebles del tipo especificado
        """
        return [m for m in self._muebles if isinstance(m, tipo_clase)]
    
    def filtrar_por_precio(self, precio_min: float = 0, precio_max: float = float('inf')) -> List['Mueble']:
        """
        Filtra muebles por rango de precios.
        
        Args:
            precio_min: Precio mínimo
            precio_max: Precio máximo
            
        Returns:
            List[Mueble]: Lista de muebles en el rango
        """
        precio_min = max(0, precio_min)
        return [m for m in self._muebles
                if precio_min <= m.calcular_precio() <= precio_max]
    
    def filtrar_por_material(self, material: str) -> List['Mueble']:
        """
        Filtra muebles por material.
        
        Args:
            material: Material a buscar
            
        Returns:
            List[Mueble]: Lista de muebles del material especificado
        """
        if not material or not material.strip():
            return []
        material_lower = material.lower().strip()
        return [m for m in self._muebles if m.material.lower() == material_lower]
    
    def filtrar_por_color(self, color: str) -> List['Mueble']:
        """
        Filtra muebles por color.
        
        Args:
            color: Color a buscar
            
        Returns:
            List[Mueble]: Lista de muebles del color especificado
        """
        if not color or not color.strip():
            return []
        color_lower = color.lower().strip()
        return [m for m in self._muebles if m.color.lower() == color_lower]
    
    def busqueda_avanzada(self, nombre: str = None, material: str = None, 
                         color: str = None, precio_min: float = 0, 
                         precio_max: float = float('inf')) -> List['Mueble']:
        """
        Realiza una búsqueda avanzada con múltiples criterios.
        
        Args:
            nombre: Nombre a buscar (opcional)
            material: Material a buscar (opcional)
            color: Color a buscar (opcional)
            precio_min: Precio mínimo
            precio_max: Precio máximo
            
        Returns:
            List[Mueble]: Lista de muebles que coinciden con todos los criterios
        """
        resultados = self._muebles
        
        if nombre and nombre.strip():
            resultados = [m for m in resultados 
                         if nombre.lower().strip() in m.nombre.lower()]
        
        if material and material.strip():
            resultados = [m for m in resultados 
                         if m.material.lower() == material.lower().strip()]
        
        if color and color.strip():
            resultados = [m for m in resultados 
                         if m.color.lower() == color.lower().strip()]
        
        precio_min = max(0, precio_min)
        resultados = [m for m in resultados 
                     if precio_min <= m.calcular_precio() <= precio_max]
        
        return resultados
    
    def ordenar_por_precio(self, descendente: bool = False) -> List['Mueble']:
        """
        Ordena los muebles por precio.
        
        Args:
            descendente: Si True, ordena de mayor a menor
            
        Returns:
            List[Mueble]: Lista ordenada por precio
        """
        return sorted(self._muebles, 
                     key=lambda m: m.calcular_precio(), 
                     reverse=descendente)
    
    def ordenar_por_nombre(self, descendente: bool = False) -> List['Mueble']:
        """
        Ordena los muebles por nombre.
        
        Args:
            descendente: Si True, ordena de Z a A
            
        Returns:
            List[Mueble]: Lista ordenada por nombre
        """
        return sorted(self._muebles, 
                     key=lambda m: m.nombre, 
                     reverse=descendente)
    
    def obtener_estadisticas(self) -> Dict:
        """
        Obtiene estadísticas del catálogo.
        
        Returns:
            Dict: Diccionario con estadísticas
        """
        if not self._muebles:
            return {
                "total_muebles": 0,
                "precio_promedio": 0,
                "precio_minimo": 0,
                "precio_maximo": 0,
                "materiales_unicos": []
            }
        
        precios = [m.calcular_precio() for m in self._muebles]
        materiales = set(m.material for m in self._muebles)
        
        return {
            "total_muebles": len(self._muebles),
            "precio_promedio": round(sum(precios) / len(precios), 2),
            "precio_minimo": round(min(precios), 2),
            "precio_maximo": round(max(precios), 2),
            "materiales_unicos": sorted(list(materiales))
        }
    
    def obtener_muebles(self) -> List['Mueble']:
        """
        Obtiene todos los muebles del catálogo.
        
        Returns:
            List[Mueble]: Copia de la lista de muebles
        """
        return self._muebles.copy()
    
    def __len__(self) -> int:
        """Retorna el número total de muebles en el catálogo."""
        return len(self._muebles)

