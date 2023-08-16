import xml.etree.ElementTree as ET

Archivo = ET.parse("D:/UNIVERSIDAD/14to Semestre/IPC2/Ejemplos/EjemplosIPC2_2sem/Clase XML/archivo.xml")

Raiz = Archivo.getroot()
'''
for elementos_encontrados in Raiz.findall('Libros_fantasia'):
    print("Libros de Fantasía")
    for libros in elementos_encontrados.findall('Libro'):
        print(" Libro:")
        for hijos in libros:
            print("     "+hijos.tag + ":" + hijos.text)
'''
'''
for elementos in Raiz:
    print("Categoria: "+elementos.tag)
    if elementos.tag == 'Libros_misterio':
        for elementos_encontrados in elementos.findall('Libro'):
            print(" Libro:")
            print(" Editorial: " + elementos_encontrados.get('editorial'))
            for hijos in elementos_encontrados:
                print("     "+hijos.tag + ":" + hijos.text)
'''

#Los pasillos aceptados solo serán los mayores a 0 y menores a 5
#Las estanterias aceptadas solo serán las mayores a 0 y menores a 3
ListaCategorias = []
for elementos in Raiz:
    Libros = []
    NombreCategoria = elementos.get('nombre')
    Pasillo = int(elementos.get('pasillo'))
    Estanteria = int(elementos.get('Estanteria'))
    if Pasillo > 0 and Pasillo < 5:
        if Estanteria > 0 and Estanteria < 3:
            for libros in elementos.findall("Libro"):
                Fila = libros.get('fila')
                Columna = libros.get('columna')
                Nombre = libros.text
                Libros.append([Fila, Columna, Nombre])
        else:
            print("La categoria "+NombreCategoria+" Fue rechazada por la estanteria "+str(Estanteria))
    else:
        print("La categoria "+NombreCategoria+" Fue rechazada por el pasillo: "+ str(Pasillo))
    ListaCategorias.append([NombreCategoria, Estanteria, Pasillo, Libros])

for Categorias in ListaCategorias:
    print(Categorias[0])
    for libros in Categorias[3]:
        print(libros[2])