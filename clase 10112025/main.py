
# from clases.persona import Persona
from clases.autoelectrico import AutoElectrico


# persona=Persona("Michael","Arjel","+56973811956","teamoinacap@inacapmail.cl")

# print(persona.getNombreCompleto())

# print (persona.correoElectronico)

# correoInsertadoConExito=persona.setCorreoElectronico="thiare.villagran@inacapmail.cl"

# if correoInsertadoConExito:
#     print("El correo se inserto sin problemas")
# else:
#     print ("algo paso con tu correo, revisa por favor ")

######## Ejericio autoElectrico ############

autoElectrico=AutoElectrico(30)

print(autoElectrico.recargar(70))

print (autoElectrico.conducir(25))
