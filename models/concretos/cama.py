"""Clase concreta para camas."""

from ..mueble import Mueble


class Cama(Mueble):
	def __init__(self, nombre, material, color, precio_base, tamaño="individual",
				 incluye_colchon=False, tiene_cabecera=True):
		super().__init__(nombre, material, color, precio_base)
		self.tamaño = tamaño
		self.incluye_colchon = bool(incluye_colchon)
		self.tiene_cabecera = bool(tiene_cabecera)

	def calcular_precio(self):
		precio = self.precio_base
		precio += {"individual": 0, "matrimonial": 150, "queen": 250,
				   "king": 350}.get(self.tamaño.lower(), 0)
		if self.incluye_colchon:
			precio += 300
		if self.tiene_cabecera:
			precio += 100
		return round(precio, 2)

	def obtener_descripcion(self):
		return (f"Cama {self.nombre} de {self.material}, color {self.color}.\n"
				f"Tamaño: {self.tamaño}\n"
				f"Colchón incluido: {'Sí' if self.incluye_colchon else 'No'}\n"
				f"Cabecera: {'Sí' if self.tiene_cabecera else 'No'}\n"
				f"Precio: ${self.calcular_precio():.2f}")
