class NodoSimple:

    def __init__(self, Dato):
        self.Dato = Dato
        self.Siguiente = None

    
    def ObtenerNombre(self):
        return self.Dato.ObtenerNombre()
    
    def ObtenerIndice(self):
        return self.Dato.ObtenerIndice()
    
    def ObtenerSiguiente(self):
        return self.Siguiente
    
    def SetSiguiente(self, NodoS):
        self.Siguiente = NodoS

    def Buscar(self, Nombre):
        return self.Dato.EncontroNombre(Nombre)