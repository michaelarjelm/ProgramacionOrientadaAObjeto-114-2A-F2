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
from .cuenta_bancaria import CuentaBancaria

SOBREGIRO_MAX=-500
class CuentaCorriente(CuentaBancaria):
    def retirar(self, monto):
        if monto<0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        if monto > super().mostrar_saldo():
            if (super().mostrar_saldo()-monto)<SOBREGIRO_MAX:
                raise ValueError("El monto a retirar es mayor que tu sobregiro")
        super().establecer_saldo(super().mostrar_saldo()-monto)
                
            
            


        
    
        