from .Nodo import *

class Cola_Fila:

    def __init__(self, nombreMatriz, tiempo, amplitud):
        self.Inicio = None
        self.Final = None
        self.Contador = 0
        self.NombreMatriz = nombreMatriz
        self.Tiempo = tiempo
        self.Amplitud = amplitud

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
                print("Filan1 [label=\"EJEMPLO 1\"] encontrada")
                #Acciones dentro de la fila
                Auxiliar.ModificarDatoColumna(columna, dato)
                return
            else:
                Auxiliar = Auxiliar.Siguiente

    def Graficar(self):
        TextoGrafica = '''subgraph Prueba1 
        {
        '''
        TextoGrafica += 'n0 [label="'+self.NombreMatriz+'"]\n\n'
        TextoGrafica += 'n1 [label="t'+str(self.Tiempo)+'"]\n'
        TextoGrafica += 'n0 -- n1;\n'
        TextoGrafica += 'n2 [label="A'+str(self.Amplitud)+'"]\n'
        TextoGrafica += 'n0 -- n2;\n\n'

        #El padre de la primera fila de la matriz es n0
        #El padre del nodo abajo de la fila n+1 es el que está en la fila anterior y la columna actual
        Auxiliar = self.Inicio
        if Auxiliar == None:
            print("No hay elementos para graficar")
        else:
            Contador = 0
            while Auxiliar != None:
                Contador += 1
                TextoGrafica += "#Fila"+str(Contador)+"\n"
                #Preguntamos si estamos en la primera fila
                if Auxiliar == self.Inicio:
                    #Si estamos en la primera fila
                    TextoGrafica += Auxiliar.Graficar("n0", True)
                else:
                    TextoGrafica += Auxiliar.Graficar("n0", False)
                Auxiliar = Auxiliar.Siguiente
            
        TextoGrafica += "}\n"
        return TextoGrafica