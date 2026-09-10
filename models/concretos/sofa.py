"""Clase concreta para sofás."""

from ..categorias.asientos import Asiento


class Sofa(Asiento):
	def __init__(self, nombre, material, color, precio_base, capacidad_personas=3,
				 tiene_respaldo=True, material_tapizado=None, es_modular=False,
				 incluye_cojines=False):
		Asiento.__init__(self, nombre, material, color, precio_base,
				 capacidad_personas, tiene_respaldo, material_tapizado)
		self.es_modular = bool(es_modular)
		self.incluye_cojines = bool(incluye_cojines)

	def calcular_precio(self):
		precio = self.precio_base * self.calcular_factor_comodidad()
		precio += 200 if self.es_modular else 0
		precio += 100 if self.incluye_cojines else 0
		return round(precio, 2)

	def obtener_descripcion(self):
		return (f"Sofá {self.nombre} de {self.material}, color {self.color}.\n"
				f"{self.obtener_info_asiento()}\n"
				f"Modular: {'Sí' if self.es_modular else 'No'}, "
				f"Cojines incluidos: {'Sí' if self.incluye_cojines else 'No'}\n"
				f"Precio: ${self.calcular_precio():.2f}")
