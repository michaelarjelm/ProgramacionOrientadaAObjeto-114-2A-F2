# Implementa una función son_anagramas(a: str, b: str) -> bool que determine 
# si dos cadenas son anagramas entre sí.

# Reglas

# Ignora espacios en blanco (espacio, tab, salto de línea).
# No distingue entre mayúsculas y minúsculas.
# Considera el resto de caracteres tal cual (letras con tilde, signos, números).

# Definición de anagrama

# Dos cadenas son anagramas si, tras normalizarlas, contienen exactamente las mismas 
# letras con la misma frecuencia.

# Requisitos
# No usar clases ni librerías externas.
# No imprimir dentro de la función.

def son_anagramas(cadenaUno:str,cadenaDos:str)->bool:
    #Aquí llevo a minusculas ambas cadenas 
    cadenaUno_min=cadenaUno.lower()
    cadenaDos_min=cadenaDos.lower()
    
    temp_cadenaUno=[]
    for caracter in cadenaUno_min:
        if not caracter.isspace():
            temp_cadenaUno.append(caracter)
    cadenaUno="".join(temp_cadenaUno)
    
    temp_cadenaDos=[]
    for caracter in cadenaDos_min:
        if not caracter.isspace():
            temp_cadenaDos.append(caracter)
    cadenaDos="".join(temp_cadenaDos)
    
    
soy_un_buleano=son_anagramas("Amor               ","              Roma")
    
    