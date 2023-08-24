from Cola.Cola_Columna import *

class Fila:

    def __init__(self, noFila, dato):
        self.NoFila = noFila
        self.ListaColumnas = Cola_Columna()
        self.Dato = dato

    def InsertarEnColumna(self, dato):
        self.ListaColumnas.Insertar(dato)
    
    def ImprimirColumnas(self):
        self.ListaColumnas.ImprimirLista()

    def DevolverFila(self):
        return self.NoFila
    
    def DevolverData(self):
        return "Esta es la fila: " + str(self.NoFila) + " El conteido es: " + self.Dato
    
    def ModificarDatoColumna(self, Columna, Dato):
        self.ListaColumnas.ModificarDato(Columna, Dato)