from Cola.Cola_Lista import *
from Graficar.Graficacion import *

print("HOLA MUNDO")

Matriz = Cola_Fila("Lista 1", 5, 4)
Matriz.Insertar("Fila 1")
Matriz.Insertar("Fila 2")
Matriz.Insertar("Fila 3")
Matriz.Insertar("Fila 4")
Matriz.Insertar("Fila 5")


Matriz.InsertarEnFila(1, 4)
Matriz.InsertarEnFila(1, 6)
Matriz.InsertarEnFila(1, 0)
Matriz.InsertarEnFila(1, 8)

Matriz.InsertarEnFila(2, 0)
Matriz.InsertarEnFila(2, 0)
Matriz.InsertarEnFila(2, 12)
Matriz.InsertarEnFila(2, 6)

Matriz.InsertarEnFila(3, 6)
Matriz.InsertarEnFila(3, 8)
Matriz.InsertarEnFila(3, 0)
Matriz.InsertarEnFila(3, 4)

Matriz.InsertarEnFila(4, 2)
Matriz.InsertarEnFila(4, 0)
Matriz.InsertarEnFila(4, 2)
Matriz.InsertarEnFila(4, 10)

Matriz.InsertarEnFila(5, 0)
Matriz.InsertarEnFila(5, 0)
Matriz.InsertarEnFila(5, 6)
Matriz.InsertarEnFila(5, 2)



Matriz.ImprimiDataEnFila(1)
Matriz.ImprimiDataEnFila(2)
Matriz.ImprimiDataEnFila(3)
Matriz.ImprimiDataEnFila(4)
Matriz.ImprimiDataEnFila(5)

def Graficar(NombreArchivo, NombreImagen):
    TextoGrafica = '''graph ""
    {
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]

    '''
    TextoGrafica += Matriz.Graficar()
    TextoGrafica += '}'
    CrearArchivo(NombreArchivo, TextoGrafica)
    CrearImagen(NombreArchivo, NombreImagen)

Graficar("ArchivoMatriz", "ImagenMatriz")

