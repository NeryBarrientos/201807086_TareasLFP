import webbrowser

arrayedad=['69','22','21','24','26','40','42','12','14','30']
arraynombres=['Nery','Jose','Luis','Fernando','Edwin','Eduardo', 'Julio','Jhotnatan','Josue','Hanssel']
arraysaldo=['230.2','1000.21','412.5','45213','1452.2','142.015','452.14','785.5','652.75','758.68']
arrayactivo=['True','False','False','False','True','True','True','True','False','True']
atributos=["Nombre","Edad","Activo","Saldo"]

def tarea(lista):
    print('Cargando Html...')
    html = '<!DOCTYPE html>\n' + '<html lang="en">\n' + '<head>\n' + '<meta charset="utf-8">\n' + '<title>Reporte Generado en HTML</title>\n'
    html = html + '</head>\n' + '<body border="2">\n'+ '<center> \n <table>\n' + '<thead>\n' + '<tr>\n'
    for i in lista:
        aux = '<th>' + i + '</th>'
        html = html + aux
    html = html + '\n</tr>' + '\n</thead>\n'
    for i in range(10):
        seguido = '<tr>\n'
        seguido = seguido + '<td>' + arraynombres[i] + '</td><td>' + arrayedad[i] + '</td><td>' + \
                   arrayactivo[i] + '</td><td>' + arraysaldo[i] + '</td>'

        seguido = seguido + '\n</tr>\n'
        html = html + seguido
    html = html + '</table>\n </center>' + '</body>\n' + '</html>'
    archivo = open("tarea.html", "w")
    archivo.write(html)
    archivo.close()

    webbrowser.open_new_tab('tarea.html')
tarea(atributos)