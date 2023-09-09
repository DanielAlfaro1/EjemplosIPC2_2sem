import TDA.Listas.ListaSimple.ListaSimple as ListaSimple
import TDA.Objetos.Dato as Dato
import TDA.Listas.ListaDoble.ListaDoble as ListaDoble

UnaListaSim = ListaSimple.ListaSimple()

UnaListaSim.ImprimirElmentos()

#Inserto primer dato
Dato1 = Dato.Dato("El Dato 1", 1)
UnaListaSim.Insertar(Dato1)
Dato2 = Dato.Dato("El Dato 2", 2)
UnaListaSim.Insertar(Dato2)
Dato3 = Dato.Dato("El Dato 3", 3)
UnaListaSim.Insertar(Dato3)
Dato4 = Dato.Dato("El Dato 4", 4)
UnaListaSim.Insertar(Dato4)

UnaListaSim.ImprimirElmentos()
print("ELIMINAMOS El elemento: El Dato 1" )
UnaListaSim.EliminarElemento("El Dato 5")
UnaListaSim.ImprimirElmentos()
print("\n")
Dato5 = Dato.Dato("El Dato 5", 5)
UnaListaSim.Insertar(Dato5)
UnaListaSim.ImprimirElmentos()


'''
UnaListaSim.ImprimirElmentos()
print("ELIMINAMOS LA POSICIÓN 3" )
UnaListaSim.EliminarIndice(0)
UnaListaSim.ImprimirElmentos()
print("\n")
Dato5 = Dato.Dato("El Dato 5", 5)
UnaListaSim.Insertar(Dato5)
UnaListaSim.ImprimirElmentos()
'''
'''
def VaciarLista(Listita):
    Listita.ImprimirElmentos()
    print("Eliminamos")
    popito = Listita.Pop()
    Listita.ImprimirElmentos()
    while popito != None:
        print("El eliminado es: ",popito.ObtenerNombre())
        print("Eliminamos")
        popito = Listita.Pop()
        Listita.ImprimirElmentos()

VaciarLista(UnaListaSim)
'''




UnaListaDoble = ListaDoble.ListaDoble()

UnaListaDoble.ImprimirElmentos()

#Inserto primer dato
Dato1 = Dato.Dato("El Dato 1", 1)
UnaListaDoble.Insertar(Dato1)
Dato2 = Dato.Dato("El Dato 2", 2)
UnaListaDoble.Insertar(Dato2)
Dato3 = Dato.Dato("El Dato 3", 3)
UnaListaDoble.Insertar(Dato3)
Dato4 = Dato.Dato("El Dato 4", 4)
UnaListaDoble.Insertar(Dato4)
'''

print("Al revés")
UnaListaDoble.ImprimirElmentosInversa()
'''
UnaListaDoble.ImprimirElmentos()
print("Errante apunta: "+UnaListaDoble.Errante.ObtenerNombre())
UnaListaDoble.MoverAdelante()
UnaListaDoble.ImprimirElmentos()
print("Errante apunta: "+UnaListaDoble.Errante.ObtenerNombre())
UnaListaDoble.MoverAdelante()
UnaListaDoble.ImprimirElmentos()
print("Errante apunta: "+UnaListaDoble.Errante.ObtenerNombre())
UnaListaDoble.MoverAdelante()
UnaListaDoble.ImprimirElmentos()
print("Errante apunta: "+UnaListaDoble.Errante.ObtenerNombre())
UnaListaDoble.MoverAdelante()
UnaListaDoble.ImprimirElmentos()
print("Errante apunta: "+UnaListaDoble.Errante.ObtenerNombre())
UnaListaDoble.MoverAtras()
UnaListaDoble.ImprimirElmentos()
print("Errante apunta: "+UnaListaDoble.Errante.ObtenerNombre())
UnaListaDoble.MoverAtras()
UnaListaDoble.ImprimirElmentos()
print("Errante apunta: "+UnaListaDoble.Errante.ObtenerNombre())
UnaListaDoble.MoverAtras()
UnaListaDoble.ImprimirElmentos()
print("Errante apunta: "+UnaListaDoble.Errante.ObtenerNombre())
UnaListaDoble.MoverAtras()
UnaListaDoble.ImprimirElmentos()
print("Errante apunta: "+UnaListaDoble.Errante.ObtenerNombre())