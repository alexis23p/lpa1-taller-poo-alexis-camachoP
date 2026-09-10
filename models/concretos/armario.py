"""Clase concreta para armarios."""

from ..categorias.almacenamiento import Almacenamiento


class Armario(Almacenamiento):
	def __init__(self, nombre, material, color, precio_base, num_puertas=2,
				 num_cajones=0, tiene_espejos=False):
		super().__init__(nombre, material, color, precio_base, num_puertas + num_cajones)
		self.num_puertas = num_puertas
		self.num_cajones = num_cajones
		self.tiene_espejos = bool(tiene_espejos)

	def calcular_precio(self):
		return round(self.precio_base + self.num_puertas * 75 + self.num_cajones * 40
					 + (150 if self.tiene_espejos else 0), 2)

	def obtener_descripcion(self):
		desc = f"Armario {self.nombre} de {self.material}, color {self.color}.\n"
		desc += f"{self.obtener_info_almacenamiento()}\n"
		desc += f"Puertas: {self.num_puertas}, Cajones: {self.num_cajones}, "
		desc += f"Espejos: {'Sí' if self.tiene_espejos else 'No'}\n"
		desc += f"Precio: ${self.calcular_precio():.2f}"
		return desc
