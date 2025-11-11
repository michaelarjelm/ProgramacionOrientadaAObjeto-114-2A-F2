import re
patro_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

class Persona:

    def __init__(self, nombre, apellido, telefono,correoElectronico):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__telefono=telefono
        self.__correoElectronico=correoElectronico

    #Este metodo es el encargado de retornar concatenado el nombre del la persona
    def getNombreCompleto(self):
        return f"{self.__nombre} {self.__apellido}"
    
    @property
    def correoElectronico(self):
        return self.__correoElectronico
    
    @correoElectronico.setter
    def setCorreoElectronico(self, nuevo_correo):
        valido=re.match(patro_correo,nuevo_correo)
        if valido:
            self.__correoElectronico=nuevo_correo
            return True
        else:
            return False
    
    




    