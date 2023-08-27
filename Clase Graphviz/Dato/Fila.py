from Cola.Cola_Columna import *

class Fila:

    def __init__(self, noFila, dato):
        self.NoFila = noFila
        self.ListaColumnas = Cola_Columna()
        self.Dato = dato #g=1(t=1,3)

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

    def Graficar(self, NodoPadre, Fila1):
        ElTextoGrafica = self.ListaColumnas.Graficar(NodoPadre, self.NoFila, Fila1)
        return ElTextoGrafica
    
    def GraficarReducida(self, NodoPadre, Fila1):
        ElTextoGrafica = "t"+str(self.NoFila)+" [label=\""+self.Dato+"\"];\n"
        ElTextoGrafica += self.ListaColumnas.Graficar(NodoPadre, self.NoFila, Fila1)
        return ElTextoGrafica