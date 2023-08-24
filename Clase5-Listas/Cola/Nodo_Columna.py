from Dato.Columna import *

class Nodo_Columna:

    def __init__(self, columna, dato):
        self.Dato = Columna(columna, dato)
        self.Siguiente = None

    def AsignarSiguiente(self, nodo_random):
        self.Siguiente = nodo_random
    
    def DevolverSiguiente(self):
        return self.Siguiente
    
    def DevolverColumna(self):
        return self.Dato.DevolverColumna()
    
    def DevolverData(self):
        return self.Dato.DevolverData()
    
    def ModificarDato(self, dato):
        self.Dato.ModificarDato(dato)