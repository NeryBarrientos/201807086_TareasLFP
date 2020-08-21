from xml.dom import minidom
import json

def xml():
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


def p_json():
    with open('datos.json') as mi_Archivo:
        datos = json.loads(mi_Archivo.read())
        print ("El tipo del archivo es:")
        print(type(datos))
        #print(datos)
        for element in datos:
                print(element)



def csv():
    with open('datos1.csv', 'r') as mi_archivocsv:
        mostrarlineas = mi_archivocsv.read().splitlines()
        print ("El tipo del archivo es")
        print (type(mostrarlineas))
        for li in mostrarlineas:
            separados = li.split(',')
            print (separados)

while True:
    print('Escoja una opcion: \n 1.Ejecute el script xml \n 2.Ejecute el script de json \n 3.Ejecute el script de csv \n 4.Salir')
    opt = input()
    if opt == '1':
        xml()
    elif opt == '2':
        p_json()
    elif opt == '3':
        csv()
    else:
        exit()
#clear()


