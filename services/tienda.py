"""
Servicio de la tienda que maneja la lógica de negocio.
Esta clase implementa el patrón de servicio para separar la lógica de negocio de la UI.
"""

from typing import List, Dict, Optional, Union
from datetime import datetime
from models.mueble import Mueble
from models.composicion.comedor import Comedor


class TiendaMuebles:
    """
    Clase que maneja toda la lógica de negocio de la tienda de muebles.
    
    Esta clase implementa:
    - Gestión de inventario
    - Búsquedas y filtros
    - Cálculos de precios y descuentos
    - Operaciones de venta
    
    Conceptos OOP aplicados:
    - Encapsulación: Agrupa toda la lógica relacionada con la tienda
    - Abstracción: Oculta la complejidad del manejo de inventario
    - Composición: Contiene colecciones de muebles
    """
    
    def __init__(self, nombre_tienda: str = "Mueblería OOP"):
        """
        Constructor de la tienda.
        
        Args:
            nombre_tienda: Nombre de la tienda
        """
        self._nombre = nombre_tienda
        self._inventario: List[Mueble] = []
        self._comedores: List[Comedor] = []
        self._ventas_realizadas: List[Dict] = []
        self._descuentos_activos: Dict[str, float] = {}
        
    
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def total_muebles(self) -> int:
        return len(self._inventario)
    
    def agregar_mueble(self, mueble: 'Mueble') -> str:
        """
        Agrega un mueble al inventario de la tienda.
        
        Args:
            mueble: Objeto mueble a agregar
            
        Returns:
            str: Mensaje de confirmación
        """
        if not isinstance(mueble, Mueble):
            return "Error: Solo se pueden agregar objetos de tipo Mueble"
        try:
            precio = mueble.calcular_precio()
            if precio <= 0:
                return "Error: El mueble debe tener un precio válido mayor a 0"
        except Exception as error:
            return f"Error al calcular precio del mueble: {error}"
        self._inventario.append(mueble)
        return f"Mueble {mueble.nombre} agregado exitosamente al inventario"
    
    def agregar_comedor(self, comedor: 'Comedor') -> str:
        """
        Agrega un comedor completo a la tienda.
        
        Args:
            comedor: Objeto Comedor a agregar
            
        Returns:
            str: Mensaje de confirmación
        """
        if not isinstance(comedor, Comedor):
            return "Error: Solo se pueden agregar objetos de tipo Comedor"
        self._comedores.append(comedor)
        return f"Comedor {comedor.nombre} agregado exitosamente"
    
    def buscar_muebles_por_nombre(self, nombre: str) -> List['Mueble']:
        """
        Busca muebles por nombre (búsqueda parcial, case-insensitive).
        
        Args:
            nombre: Nombre o parte del nombre a buscar
            
        Returns:
            List[Mueble]: Lista de muebles que coinciden con la búsqueda
        """
        if not nombre or not nombre.strip():
            return []
        termino = nombre.lower().strip()
        return [mueble for mueble in self._inventario if termino in mueble.nombre.lower()]
    
    def filtrar_por_precio(self, precio_min: float = 0, precio_max: float = float('inf')) -> List['Mueble']:
        """
        Filtra muebles por rango de precios.
        
        Args:
            precio_min: Precio mínimo (inclusivo)
            precio_max: Precio máximo (inclusivo)
            
        Returns:
            List[Mueble]: Lista de muebles en el rango de precios
        """
        precio_min = max(0, precio_min)
        return [mueble for mueble in self._inventario
            if precio_min <= mueble.calcular_precio() <= precio_max]
    
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
        return [mueble for mueble in self._inventario
            if mueble.material.lower() == material_lower]
    
    def obtener_muebles_por_tipo(self, tipo_clase: type) -> List['Mueble']:
        """
        Obtiene todos los muebles de un tipo específico.
        
        Args:
            tipo_clase: Clase del tipo de mueble (ej: Silla, Mesa, etc.)
            
        Returns:
            List[Mueble]: Lista de muebles del tipo especificado
        """
        return [mueble for mueble in self._inventario if isinstance(mueble, tipo_clase)]
    
    def calcular_valor_inventario(self) -> float:
        """
        Calcula el valor total del inventario.
        
        Returns:
            float: Valor total de todos los muebles en inventario
        """
        valor_total = sum(mueble.calcular_precio() for mueble in self._inventario)
        valor_total += sum(comedor.calcular_precio_total() for comedor in self._comedores)
        return round(valor_total, 2)
    
    def aplicar_descuento(self, categoria: str, porcentaje: float) -> str:
        """
        Aplica un descuento a una categoría de muebles.
        
        Args:
            categoria: Nombre de la categoría (ej: "sillas", "mesas")
            porcentaje: Porcentaje de descuento (0-100)
            
        Returns:
            str: Mensaje de confirmación
        """
        if not 0 <= porcentaje <= 100:
            return "Error: El porcentaje debe estar entre 0 y 100"
        categoria_lower = categoria.lower().strip()
        if not categoria_lower:
            return "Error: La categoría no puede estar vacía"
        self._descuentos_activos[categoria_lower] = porcentaje / 100
        return f"Descuento del {porcentaje}% aplicado a la categoría '{categoria}'"
    
    def realizar_venta(self, mueble: 'Mueble', cliente: str = "Cliente Anónimo") -> Dict:
        """
        Procesa la venta de un mueble.
        
        Args:
            mueble: Mueble a vender
            cliente: Nombre del cliente
            
        Returns:
            Dict: Información de la venta realizada
        """
        if mueble not in self._inventario:
            return {"error": "El mueble no está disponible en inventario"}
        try:
            precio_original = mueble.calcular_precio()
            descuento = self._descuentos_activos.get(type(mueble).__name__.lower(), 0)
            venta = {
                "mueble": mueble.nombre,
                "cliente": cliente,
                "precio_original": precio_original,
                "descuento": descuento * 100,
                "precio_final": round(precio_original * (1 - descuento), 2),
                "fecha": datetime.now().isoformat(timespec="seconds"),
            }
            self._inventario.remove(mueble)
            self._ventas_realizadas.append(venta)
            return venta
        except Exception as error:
            return {"error": f"Error al procesar la venta: {error}"}
    
    def obtener_estadisticas(self) -> Dict:
        """
        Obtiene estadísticas generales de la tienda.
        
        Returns:
            Dict: Diccionario con estadísticas de la tienda
        """
        return {
            "total_muebles": len(self._inventario),
            "total_comedores": len(self._comedores),
            "valor_inventario": self.calcular_valor_inventario(),
            "ventas_realizadas": len(self._ventas_realizadas),
            "tipos_muebles": self._contar_tipos_muebles(),
            "descuentos_activos": len(self._descuentos_activos),
        }
    
    def _contar_tipos_muebles(self) -> Dict[str, int]:
        """
        Cuenta cuántos muebles hay de cada tipo.
        Método privado auxiliar.
        
        Returns:
            Dict[str, int]: Diccionario con el conteo por tipo
        """
        conteo = {}
        for mueble in self._inventario:
            tipo = type(mueble).__name__
            conteo[tipo] = conteo.get(tipo, 0) + 1
        return conteo
    
    def generar_reporte_inventario(self) -> str:
        """
        Genera un reporte completo del inventario.
        
        Returns:
            str: Reporte detallado del inventario
        """
        estadisticas = self.obtener_estadisticas()
        reporte = f"=== REPORTE DE INVENTARIO - {self.nombre} ===\n\n"
        reporte += f"Total de muebles: {estadisticas['total_muebles']}\n"
        reporte += f"Total de comedores: {estadisticas['total_comedores']}\n"
        reporte += f"Valor total del inventario: ${estadisticas['valor_inventario']:.2f}\n\n"
        reporte += "DISTRIBUCIÓN POR TIPOS:\n"
        for tipo, cantidad in estadisticas["tipos_muebles"].items():
            reporte += f"- {tipo}: {cantidad} unidades\n"
        if self._descuentos_activos:
            reporte += "\nDESCUENTOS ACTIVOS:\n"
            for categoria, descuento in self._descuentos_activos.items():
                reporte += f"- {categoria}: {descuento * 100:.1f}%\n"
        return reporte

