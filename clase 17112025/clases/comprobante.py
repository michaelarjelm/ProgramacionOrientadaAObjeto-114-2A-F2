# Parte 2 – Subclase Comprobante

# Crea la clase Comprobante, que herede de Documento.
# Agrega un atributo privado __monto.
# Usa @property y @setter para que el monto siempre sea mayor que 0.
# En su constructor (__init__), usa super().__init__(...) 
# para inicializar los atributos heredados.
from clases.documento import Documento
class Comprobante(Documento):
    def __init__(self, id,fecha, monto):
        super().__init__(id,fecha)
        self.__monto=monto
    
    @property
    def monto(self):
        return self.__monto
    
    @monto.setter
    def monto(self, monto):
        if monto<0:
            raise Exception("El monto debe ser mayor a 0")
        self.__monto=monto
