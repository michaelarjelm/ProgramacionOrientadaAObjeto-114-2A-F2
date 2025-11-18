# 🧾 Ejercicio – Sistema de Comprobantes Contables
# En una empresa se necesita modelar el sistema de documentos contables, donde cada tipo de documento agrega información adicional sobre el anterior. El objetivo es aplicar herencia multinivel y encapsulamiento, asegurando que los datos cumplan reglas básicas de validación.

# Parte 1 – Clase base Documento

# Define una clase Documento que represente cualquier documento contable. OK
# Debe tener los siguientes atributos privados:
# __id → número identificador del documento.
# __fecha → fecha de emisión en formato texto (por ejemplo, "2025-09-07").
# Aplica encapsulamiento con @property y @setter para validar:
# El id debe ser mayor que 0.
# La fecha no puede estar vacía.
# Parte 2 – Subclase Comprobante

# Crea la clase Comprobante, que herede de Documento.
# Agrega un atributo privado __monto.
# Usa @property y @setter para que el monto siempre sea mayor que 0.
# En su constructor (__init__), usa super().__init__(...) para inicializar 
# los atributos heredados.

#from datetime import date

class Documento:
    def __init__(self, id, fecha):
        self.__id=id
        self.__fecha=fecha

    @property    
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        if id<0:
            raise Exception("El id debe ser mayor a 0")
        self.__id=id

    @property    
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self,fecha):
        if fecha=="":
            raise Exception("La fecha no puede estar vacía")
        self.__fecha=fecha
        
    