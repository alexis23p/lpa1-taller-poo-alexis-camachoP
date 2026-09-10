"""Clase concreta para cajoneras."""

from ..categorias.almacenamiento import Almacenamiento


class Cajonera(Almacenamiento):
	def __init__(self, nombre, material, color, precio_base, num_cajones=3,
				 tiene_ruedas=False):
		super().__init__(nombre, material, color, precio_base, num_cajones)
		self.num_cajones = num_cajones
		self.tiene_ruedas = bool(tiene_ruedas)

	def calcular_precio(self):
		return round(self.precio_base + self.num_cajones * 35 + (50 if self.tiene_ruedas else 0), 2)

	def obtener_descripcion(self):
		desc = f"Cajonera {self.nombre} de {self.material}, color {self.color}.\n"
		desc += f"{self.obtener_info_almacenamiento()}\n"
		desc += f"Ruedas: {'Sí' if self.tiene_ruedas else 'No'}\n"
		desc += f"Precio: ${self.calcular_precio():.2f}"
		return desc
