from .Nodo import *

class Cola_Fila:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0

    def Insertar(self, Dato):
        self.Contador += 1
        NuevoNodo =  Nodo_Fila(self.Contador, Dato)
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

    def InsertarEnFila(self, indice, dato):
        Contador = 0
        Auxiliar = self.Inicio
        if indice == 0 or indice > self.Contador:
            return
        while Auxiliar != None:
            Contador += 1
            if Contador == indice:
                Auxiliar.InsertarEnColunma(dato)
                return
            else:
                Auxiliar = Auxiliar.Siguiente
    
    def ImprimiDataEnFila(self, indice):
        Contador = 0
        Auxiliar = self.Inicio
        if indice == 0 or indice > self.Contador:
            return
        while Auxiliar != None:
            Contador += 1
            if Contador == indice:
                Auxiliar.ImprimirListaColumna()
                return
            else:
                Auxiliar = Auxiliar.Siguiente

    def ModificarDatoColumna(self, fila, columna, dato):
        Contador = 0
        Auxiliar = self.Inicio
        if fila == 0 or fila > self.Contador:
            print("No existe la fila buscada")
            return 
        while Auxiliar != None:
            Contador += 1
            if Contador == fila:
                print("Fila encontrada")
                #Acciones dentro de la fila
                Auxiliar.ModificarDatoColumna(columna, dato)
                return
            else:
                Auxiliar = Auxiliar.Siguiente