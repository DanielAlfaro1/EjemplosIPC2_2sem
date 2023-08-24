import random
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def ObtenerNums(cantidadX, cantidadY):
    contenido = ""
    historial = []
    for X in range(cantidadX):
        SeCopia = round(random.random()*10)
        if (SeCopia == 2 or SeCopia == 4 or SeCopia == 9) and len(historial) > 0:
            print("Hay copia")
            for Y in range(cantidadY):
                if Y == 0:
                    contenido = contenido + str(round(random.random()*historial[Y]))
                else:
                    contenido = contenido + "," + str(round(random.random()*historial[Y]))
            if X != cantidadX-1:
                contenido = contenido + "\n"
            historial = []
        else:
            for Y in range(cantidadY):
                ayudante = round(random.random()*10)
                multiplo = 100
                if ayudante == 1 or ayudante == 7 or ayudante == 8 or ayudante == 3:
                    multiplo = 0
                historial.append(multiplo)
                if Y == 0:
                    contenido = contenido + str(round(random.random()*multiplo))
                else:
                    contenido = contenido + "," + str(round(random.random()*multiplo))
            if X != cantidadX-1:
                contenido = contenido + "\n"

    return contenido

def ObtenerHeaders(cantidadX, cantidadY, numeros):
    listaFilas = numeros.split("\n")
    Filas = ""
    Columnas = "Tiempo (seg)"
    EncabezadoPrincipal = "Amplitud (db)"
    for Y in range(cantidadY):
        Columnas = Columnas + "," + str(Y+1)
        EncabezadoPrincipal = EncabezadoPrincipal + ","
    Filas = EncabezadoPrincipal + "\n"
    Filas = Filas + Columnas + "\n"
    for X in range(cantidadX):
        Filas = Filas + str(X+1) + "," +listaFilas[X]+"\n"
    return Filas


def GenerarCSV(Contenido, Nombre):
    if os.path.isdir("Proyecto 1"):
        archivo = open("Proyecto 1/"+Nombre+".csv", "w")
        archivo.write(Contenido)
        archivo.close()
    else:
        os.makedirs("Proyecto 1")
        archivo = open("Proyecto 1/"+Nombre+".csv", "w")
        archivo.write(Contenido)
        archivo.close()

def GenerarSenalXML(t, A, Numeros, Nombre):
    ListaNumeros = Numeros.split("\n")
    raiz = ET.Element('senal')
    raiz.set("nombre", Nombre)
    raiz.set("t", str(t))
    raiz.set("A", str(A))
    for fila in range(t):
        NumerosFila = ListaNumeros[fila].split(",")
        for columna in range(A):
            dato = ET.SubElement(raiz, "dato")
            dato.text =  NumerosFila[columna]
            dato.set("t", str(fila + 1))
            dato.set("A", str(columna + 1))
    return raiz
    


def GenerarArchivoEntrada(Cantidad, Prefijo, base10, limite_t, limite_A):
    raiz = ET.Element('senales')
    
    for senal in range(Cantidad):
        t = round(random.random()*base10)
        print(t)
        while t <= 1 or t > limite_t:
            t = round(random.random()*base10)
            print(t)
        A = round(random.random()*base10)
        print("A",A)
        while A <= 1 or A > limite_A:
            A = round(random.random()*base10)
            print("A",A)
        numeros = ObtenerNums(t, A)
        contenidoCSV = ObtenerHeaders(t, A, numeros)
        GenerarCSV(contenidoCSV, Prefijo + str(senal + 1))
        nodo = GenerarSenalXML(t, A, numeros, Prefijo + str(senal + 1))
        raiz.append(nodo)

    xmlstr = minidom.parseString(ET.tostring(raiz)).toprettyxml(indent="\t")
    with open("Proyecto 1/Entrada-Ejemplo.xml", "w") as f:
        f.write(xmlstr)


# Cantidad es la cantidad de señales que se generarán
# Prefijo es el prefijo del nombre de los archivos CSV que se van a generar
# base10 es un número en base 10 (10, 100, 1000)    
# limite_t es un número del cual t no va a pasar
# limite_A es un número del cual A no va a pasar
GenerarArchivoEntrada(Cantidad=5, Prefijo="Ejemplo", base10=10, limite_t=5, limite_A=5)