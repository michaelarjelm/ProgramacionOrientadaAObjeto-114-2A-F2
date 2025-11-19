# Parte 4 – Demostración

# Crea una Factura válida con:
# id = 101
# fecha = "2025-09-07"
# monto = 150000
# rut_cliente = "12.345.678-9"
# Llama a resumen_factura() y muestra el resultado en pantalla.
# Intenta asignar un monto negativo y captura la excepción 
# lanzada por el setter, demostrando que el encapsulamiento 
# está funcionando.


from clases.factura import Factura

factura=Factura("FAC-001","2025-11-18",180000,"9539332-2")

print(factura.resumen_factura())







