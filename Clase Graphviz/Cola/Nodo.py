from .Cola_Columna import *
from Dato.Fila import *

class Nodo_Fila:

    def __init__(self, fila, dato):
        self.Dato = Fila(fila, dato)
        self.Siguiente = None

    def AsignarSiguiente(self, nodo_random):
        self.Siguiente = nodo_random
    
    def DevolverSiguiente(self):
        return self.Siguiente
    
    def DevolverFila(self):
        return self.Dato.DevolverFila()
    
    def DevolverData(self):
        return self.Dato.DevolverData()
    
    def InsertarEnColunma(self, Dato):
        self.Dato.InsertarEnColumna(Dato)
    
    def ImprimirListaColumna(self):
        self.Dato.ImprimirColumnas()

    def ModificarDatoColumna(self, Columna, dato):
        self.Dato.ModificarDatoColumna(Columna, dato)

    def Graficar(self, nodoPadre, Fila1):
        return self.Dato.Graficar(nodoPadre, Fila1)