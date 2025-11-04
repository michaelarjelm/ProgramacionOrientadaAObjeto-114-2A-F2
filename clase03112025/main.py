
# Crea una clase llamada Circulo que tenga:OK

# Un constructor que reciba el radio como parámetro.OK
# Un método llamado área que calcule y devuelva el 
# área del círculo (usa la fórmula: área = π * radio^2).

# Instrucciones:

# Crea una instancia de Circulo con radio 5.
# Llama al método área e imprime el resultado.

#from clases.circulo import Circulo
from clases.cuentaBancaria import CuentaBancaria

# timonYPumba=Circulo(5)


# print(round(timonYPumba.area(),2))

cuentaBancaria=CuentaBancaria("123456","Lilian Labbe", 25000)

print (cuentaBancaria.mostrar_datos())

cuentaBancaria.depositar(1000000)

print (cuentaBancaria.mostrar_datos())

cuentaBancaria.retirar(1000000)

