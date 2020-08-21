from xml.dom import minidom

acceso = minidom.parse("datos2.xml")
Nombretodos = acceso.getElementsByTagName("estudiante")
print ("El tipo de archivo es:")
print (type(acceso))
print ()
for element in Nombretodos:
    nombre = element.getElementsByTagName("nombre")[0]
    apellido = element.getElementsByTagName("apellido")[0]
    edad = element.getElementsByTagName("edad")[0]
    residencia = element.getElementsByTagName("residencia")[0]
    print ("El nombre es:", nombre.firstChild.data)
    print("El apellido es:", apellido.firstChild.data)
    print("La edad es:", edad.firstChild.data)
    print("Su residencia es en:", residencia.firstChild.data)
    print ()
