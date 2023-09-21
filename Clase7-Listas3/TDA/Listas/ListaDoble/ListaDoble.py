from .Nodo_Doble import NodoDoble

class ListaDoble:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Errante = None

    def Insertar(self, Dato):
        NuevoNodo = NodoDoble(Dato)

        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.Errante = NuevoNodo
        else:
            self.Final.SetSiguiente(NuevoNodo)
            NuevoNodo.SetAnterior(self.Final)
            self.Final = NuevoNodo

    def InsertarIndice(self, Dato, indice):
        #indice será un valor numérico, que indica la posición de la lista donde vamos a colocar un nuevo dato, la primera posición será 0
        if self.Inicio == None:
            if indice == 0:
                #Insertamos en la primera posición de la lista
                NuevoNodo = NodoDoble(Dato)
                self.Inicio = NuevoNodo
                self.Final = NuevoNodo
                self.Errante = NuevoNodo
                return None

            print("La lista está vacía, el indice no apunta a la primera posición entonces no inserta nada.")
            return None
        if indice < 0:
            print("No se pueden eliminar posiciones menores a 0")
            return None
        if indice == 0:
            NuevoNodo = NodoDoble(Dato)
            NuevoNodo.Siguiente = self.Inicio
            self.Inicio.Anterior = NuevoNodo
            self.Inicio = NuevoNodo
            return None
        Auxiliar = self.Inicio
        Contador = 0
        Auxliar2 = None
        while Auxiliar != None:
            if Contador == indice:
                NuevoNodo = NodoDoble(Dato)
                NuevoNodo.Siguiente = Auxiliar
                NuevoNodo.Anterior = Auxliar2
                Auxiliar.Anterior = NuevoNodo
                Auxliar2.Siguiente = NuevoNodo
                return None
            Auxliar2 = Auxiliar
            Auxiliar = Auxiliar.ObtenerSiguiente()
            Contador += 1
        print("No existe la posición indicada")
        return None

    def Pop(self):
        if self.Inicio != None:
            if self.Inicio.ObtenerSiguiente() == None:
                Auxiliar = self.Inicio
                self.Inicio = None
                self.Final = None
                return Auxiliar
            else:
                Auxiliar = self.Inicio
                self.Inicio = self.Inicio.ObtenerSiguiente()
                Auxiliar.SetSiguiente(None)
                return Auxiliar
            
    def EliminarIndice(self, indice):
        #indice será un valor numérico, que indica la posición de la lista a eliminar, la primera posición será 0
        if self.Inicio == None:
            print("La lista está vacía, no se puede eliminar nada.")
            return None
        if indice < 0:
            print("No se pueden eliminar posiciones menores a 0")
            return None
        if indice == 0:
            Auxiliar = self.Pop()
            return Auxiliar
        Auxiliar = self.Inicio
        Contador = 0
        Auxliar2 = None
        while Auxiliar != None:
            if Contador == indice:
                if Auxiliar == self.Final:
                    self.Final = Auxliar2
                Auxliar2.SetSiguiente(Auxiliar.ObtenerSiguiente())
                Auxiliar.SetSiguiente(None)
                print("Se eliminó la posicion requerida")
                return Auxiliar
            Auxliar2 = Auxiliar
            Auxiliar = Auxiliar.ObtenerSiguiente()
            Contador += 1
        print("No existe la posición indicada")
        return None
            
    def EliminarElemento(self, Nombre):
        #indice será un valor numérico, que indica la posición de la lista a eliminar, la primera posición será 0
        if self.Inicio == None:
            print("La lista está vacía, no se puede eliminar nada.")
            return None
        if self.Inicio.Buscar(Nombre):
            Auxiliar = self.Pop()
            return Auxiliar
        Auxiliar = self.Inicio
        Auxliar2 = None
        while Auxiliar != None:
            if Auxiliar.Buscar(Nombre):
                if Auxiliar == self.Final:
                    self.Final = Auxliar2
                Auxliar2.SetSiguiente(Auxiliar.ObtenerSiguiente())
                Auxiliar.SetSiguiente(None)
                print("Se eliminó el elemento solicitado")
                return Auxiliar
            Auxliar2 = Auxiliar
            Auxiliar = Auxiliar.ObtenerSiguiente()
        print("No existe el elemento con ese filtro.")
        return None
    
    def ImprimirElmentos(self):
        if self.Inicio != None:
            Auxiliar = self.Inicio
            while Auxiliar != None:
                print("Nombre:",Auxiliar.ObtenerNombre(),"Indice:",Auxiliar.ObtenerIndice())
                Auxiliar = Auxiliar.ObtenerSiguiente()
        else:
            print("Lista Vacía")

    def ImprimirElmentosInversa(self):
        if self.Final != None:
            Auxiliar = self.Final
            while Auxiliar != None:
                print("Nombre:",Auxiliar.ObtenerNombre(),"Indice:",Auxiliar.ObtenerIndice())
                Auxiliar = Auxiliar.ObtenerAnterior()
        else:
            print("Lista Vacía")

    def MoverAdelante(self):
        if self.Errante.ObtenerSiguiente() != None:
            self.Errante = self.Errante.Siguiente
        else:
            print("YA NO HAY MÁS POSICIONES")

    def MoverAtras(self):
        if self.Errante.ObtenerAnterior() != None:
            self.Errante = self.Errante.Anterior
        else:
            print("YA NO HAY MÁS POSICIONES")