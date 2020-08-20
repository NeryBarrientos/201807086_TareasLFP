import json

with open('datos.json') as mi_Archivo:
    datos = json.loads(mi_Archivo.read())
print ("El tipo de la lista es:")
print(type(datos))
#print(datos)
for element in datos:
    print(element)
