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