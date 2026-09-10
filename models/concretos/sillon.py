"""Clase concreta para sillones."""

from ..categorias.asientos import Asiento


class Sillon(Asiento):
	def __init__(self, nombre, material, color, precio_base, tiene_respaldo=True,
				 material_tapizado=None, es_reclinable=False, tiene_reposapiés=False):
		super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo,
						 material_tapizado)
		self.es_reclinable = bool(es_reclinable)
		self.tiene_reposapiés = bool(tiene_reposapiés)

	def calcular_precio(self):
		precio = self.precio_base * self.calcular_factor_comodidad()
		precio += 250 if self.es_reclinable else 0
		precio += 100 if self.tiene_reposapiés else 0
		return round(precio, 2)

	def obtener_descripcion(self):
		return (f"Sillón {self.nombre} de {self.material}, color {self.color}.\n"
				f"{self.obtener_info_asiento()}\nPrecio: ${self.calcular_precio():.2f}")
