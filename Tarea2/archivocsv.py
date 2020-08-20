with open('datos1.csv', 'r') as mi_archivocsv:
    mostrarlineas = mi_archivocsv.read().splitlines()
    for li in mostrarlineas:
        separados = li.split(',')
        print (separados)