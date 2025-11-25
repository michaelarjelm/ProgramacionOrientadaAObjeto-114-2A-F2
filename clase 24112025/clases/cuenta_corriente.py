# 📌 Ejercicio 1 – Cuentas bancarias
# Crea una clase base CuentaBancaria con:
# Atributo privado __saldo.
# Métodos depositar(monto) y retirar(monto) 
# con validación (no permitir montos negativos, 
# ni saldo insuficiente).
# Método mostrar_saldo() que devuelve el saldo.
# Subclases:
# CuentaAhorro → gana un interés de 2% cuando se consulta el saldo. 
# CuentaCorriente → permite sobregiro de hasta -500.
# 👉 Recorre una lista de cuentas y llama a mostrar_saldo() 
# en cada una, mostrando polimorfismo.
from cuenta_bancaria import CuentaBancaria

SOBREGIRO=500
class CuentaCorriente(CuentaBancaria):
    def retirar(self, monto):
        if monto<0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        