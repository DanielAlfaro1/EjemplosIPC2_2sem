from .Nodo_Columna import *

class Cola_Columna:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0

    def Insertar(self, Dato):
        self.Contador += 1
        NuevoNodo =  Nodo_Columna(self.Contador, Dato)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
    
    def ImprimirLista(self):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            print(Auxiliar.DevolverData())
            Auxiliar = Auxiliar.Siguiente
        print("Terminó de imprimir lista")

    def ModificarDato(self, columna, dato):
        Contador = 0
        Auxiliar = self.Inicio
        if columna == 0 or columna > self.Contador:
            print("No existe la columna")
            return
        else:
            while Auxiliar != None:
                Contador += 1
                if Contador == columna:
                    print("Encontramos columna")
                    #Modificamos dato
                    Auxiliar.ModificarDato(dato)
                else:
                    Auxiliar = Auxiliar.Siguiente