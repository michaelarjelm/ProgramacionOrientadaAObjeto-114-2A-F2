# Diseñe un sistema para gestionar la información de 
# una veterinaria. Cada mascota debe estar identificada 
# por su nombre, especie y edad. La veterinaria debe permitir 
# registrar nuevas mascotas en su registro, buscar una mascota 
# específica por su nombre, consultar en cualquier momento el 
# listado completo de todas las mascotas atendidas y obtener la
# edad promedio de las mascotas registradas.
# Requerimientos funcionales
# El sistema debe permitir registrar una nueva mascota, indicando su nombre, 
# especie y edad.
# El sistema debe permitir consultar el listado completo de mascotas, 
# mostrando los datos principales de cada una.
# El sistema debe permitir buscar una mascota por su nombre, mostrando 
# su información si existe en el registro.
# Si se intenta buscar una mascota que no existe, el sistema debe 
# informarlo claramente.
# El sistema debe permitir calcular la edad promedio de las mascotas 
# registradas en la veterinaria.
# Si no hay mascotas registradas y se intenta calcular la edad promedio, 
# el sistema debe indicar que no es posible realizar el cálculo.
# El sistema debe ofrecer una forma de visualizar el estado actualizado 
# del registro, incluyendo el total de mascotas y, cuando sea relevante, 
# la edad promedio.

from mascota import Mascota
class Veterinaria:
    def __init__(self, nombreVeterinaria):
        self.nombreVeterinaria=nombreVeterinaria
        self.mascotas=[]
        
    def registrar_mascota(self, mascota:Mascota):
        self.mascotas.append(mascota)
        