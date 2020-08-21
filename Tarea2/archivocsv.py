with open('datos1.csv', 'r') as mi_archivocsv:
    mostrarlineas = mi_archivocsv.read().splitlines()
    print ("El tipo del archivo es")
    print (type(mostrarlineas))
    for li in mostrarlineas:
        separados = li.split(',')
        print (separados)