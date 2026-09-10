"""Clase concreta para escritorios."""

from ..categorias.superficies import Superficie


class Escritorio(Superficie):
	def __init__(self, nombre, material, color, precio_base, forma="rectangular",
				 tiene_cajones=False, num_cajones=0, tiene_iluminacion=False):
		super().__init__(nombre, material, color, precio_base, forma, 1)
		self.tiene_cajones = bool(tiene_cajones)
		self.num_cajones = num_cajones if tiene_cajones else 0
		self.tiene_iluminacion = bool(tiene_iluminacion)

	def calcular_precio(self):
		return round(self.precio_base * self.calcular_factor_estabilidad() 
					 + self.num_cajones * 40
					 + (100 if self.tiene_iluminacion else 0), 2)

	def obtener_descripcion(self):
		desc = f"Escritorio {self.nombre}, forma {self.forma}.\n"
		desc += f"{self.obtener_info_superficie()}\n"
		if self.tiene_cajones:
			desc += f"Cajones: {self.num_cajones}\n"
		desc += f"Iluminación: {'Sí' if self.tiene_iluminacion else 'No'}\n"
		desc += f"Precio: ${self.calcular_precio():.2f}"
		return desc
