
# Parte 3 – Subclase Factura

# Crea la clase Factura, que herede de Comprobante.OK
# Agrega un atributo privado __rut_cliente.
# Define un método resumen_factura() que:
# Use los getters heredados (id, fecha, monto).
# Devuelva un texto con el formato: 
# “Factura ID: 101 | Fecha: 2025-09-07 | Monto: $150000 | 
# Cliente: 12.345.678-9"
# En su constructor (__init__), usa super().__init__(...) 
# para inicializar lo heredado, y luego inicializa __rut_cliente.
from clases.comprobante import Comprobante

class Factura(Comprobante):
    def __init__(self, id, fecha, monto, rutCliente):
        super().__init__(id, fecha, monto)
        self.__rutCliente=rutCliente
    
    
    def resumen_factura(self):
        return f"Factura {super().id} | Fecha {super().fecha} | Monto {super().monto} | {self.__rutCliente}"
