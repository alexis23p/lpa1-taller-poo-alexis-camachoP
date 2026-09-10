"""Clase concreta para mesas."""

from ..categorias.superficies import Superficie


class Mesa(Superficie):
	def __init__(self, nombre, material, color, precio_base, forma="rectangular",
				 capacidad_personas=4):
		super().__init__(nombre, material, color, precio_base, forma, capacidad_personas)

	def calcular_precio(self):
		return round(self.precio_base * self.calcular_factor_estabilidad() * ({"redonda": 1.05, "L": 1.15}.get(self.forma, 1.0)), 2)

	def obtener_descripcion(self):
		return (f"Mesa {self.nombre} de {self.material}, color {self.color}.\n"
				f"{self.obtener_info_superficie()}\n"
				f"Precio: ${self.calcular_precio():.2f}")
