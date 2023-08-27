class Columna:
    
    def __init__(self, columna, dato):
        self.Columna = columna
        self.Dato = dato
    
    def DevolverColumna(self):
        return self.Columna
    
    def DevolverData(self):
        return self.Dato
    
    def ModificarDato(self, dato):
        self.Dato = dato

    def Graficar(self, NodoPadre, NoFila, Fila1):
        #F[NO. FILA]C[NO. COLUMNA]
        ElTextoGrafica = 'F'+str(NoFila)+'C'+str(self.Columna)+' [label="'+str(self.Dato)+'"];\n'
        if Fila1:
            ElTextoGrafica += ''+NodoPadre+' -- '+'F'+str(NoFila)+'C'+str(self.Columna)+';\n'
        else:
            ElTextoGrafica += 'F'+str(NoFila-1)+'C'+str(self.Columna)+' -- '+'F'+str(NoFila)+'C'+str(self.Columna)+';\n'
        return ElTextoGrafica