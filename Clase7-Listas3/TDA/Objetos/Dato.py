
class Dato:

    def __init__(self, nombre, indice):
        self.Nombre = nombre
        self.Indice = indice

    def ObtenerNombre(self):
        return self.Nombre
    
    def ObtenerIndice(self):
        return self.Indice
    
    def EncontroNombre(self, Nombre):
        if self.Nombre == Nombre:
            return True
        return False