from Cola.Cola_Lista import *

print("HOLA MUNDO")

NuevaLista = Cola_Fila()
NuevaLista.Insertar("Cualquier cosa")
NuevaLista.Insertar("Cualquier cosa")
NuevaLista.Insertar("Cualquier cosa")

NuevaLista.ImprimirLista()

#INSERTAMOS DATOS EN LA FILA 1, FILA 2 Y FILA 3
NuevaLista.InsertarEnFila(2,"Esta es la fila 2 y el dato 1")
NuevaLista.InsertarEnFila(3,"Esta es la fila 3 y el dato 1")
NuevaLista.InsertarEnFila(1,"Esta es la fila 1 y el dato 1")
NuevaLista.InsertarEnFila(2,"Esta es la fila 2 y el dato 2")

NuevaLista.ImprimiDataEnFila(1)
NuevaLista.ImprimiDataEnFila(2)
NuevaLista.ImprimiDataEnFila(3)

#MODIFICAMOS DATO EN FILA 2 Y COLUMNA 2
NuevaLista.ModificarDatoColumna(2, 2, "Esta es la fila 2 y el dato nuevo")

NuevaLista.ImprimiDataEnFila(1)
NuevaLista.ImprimiDataEnFila(2)
NuevaLista.ImprimiDataEnFila(3)