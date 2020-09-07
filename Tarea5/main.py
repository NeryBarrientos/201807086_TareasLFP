print("Elija una opcion: \n1. __servidor1 \n2. 3servidor")
opcion = input()
palabra = ''
pos = 0
a = '_'
def opcion_palabra():
    if int(opcion) == 1:
        return '__servidor1'
    elif int(opcion) == 2:
        return '3servidor'
    else:
        print("Escoge una opcion valida")
        opcion_palabra()

def estado0(pal,pos):
    if pal[pos] == '_':
        pos += 1
        estado1(pal,pos)
    else:
        print("Eror de sintaxis")

def estado1(pal,pos):
    try:
        n = int(pal[pos])
        estado3(n,pos)
    except:
        if pal[pos] == '_':
            pos += 1
            estado1(pal,pos)
        elif type(pal[pos]) == str:
            pos += 1
            estado1(pal,pos)

def estado3(pal,pos):
    if type(pal) == int:
        print("La cadena es correcta")
    else:
        print("Incorrecto")


palabra = opcion_palabra()
x = estado0(palabra,pos)
