# Atributo privado 	bateria (nivel de carga, de 0 a 100).OK
# Método cargar(energia) que aumente la batería
# hasta un máximo de 100.
# Método conducir(km) que reduzca la batería (1 km = 1%).
# Simula conducir 30 km y luego cargar 50%.

class AutoElectrico:
    def __init__(self, bateria):
        self.__bateria=bateria
        
    
        
    def recargar(self, recarga):
            if recarga <=0:
                return "El valor a cargar debe ser mayor a 0"
            elif (recarga+self.__bateria)>100:
                return F"El valor recargado supera el máximo de capacidad, se recargaron {100-self.__bateria}%, por lo tanto se le devolverá lo equivalente a {(self.__bateria+recarga)-100}% en dinero"
            else:
                self.__bateria=self.__bateria+recarga
                return f"Recarga realizada con éxito, nuevo porcentaje de batería {self.__bateria}%" 
    def conducir(self, km):
        if km <=0:
            return "El valor ingresado debe ser mayor a 0"
        elif km>self.__bateria:
            return f"Usted no puede conducir {km} kilometros, su porcentaje de batería es insuficiente"
        else:
            self.__bateria=self.__bateria-km
            return f"Condujiste {km} kilometros, te queda un {self.__bateria}% de bateria"


        
        
        

        
        
    