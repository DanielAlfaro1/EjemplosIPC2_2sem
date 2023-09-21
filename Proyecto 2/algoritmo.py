'''
ListaSistemasDrones = Lista()

Lectura xml:
    Leemos lista sistema drones:
        mientras Leer sistema dron:
            Nombre = leer atributo nombre sistema dron.
            Altura = leer altura maxima sistema dron
            NoDrones = leer cantidad drones sistema dron
            SistemaDrones = ListaDrones(Nombre, Altura, NoDrones)
            mientras leemos contenido:
                Nombre_Dron = leer dron
                Dron = ListaAlturas(Nombre_Dron)
                Altura0 = Altura(0, 'vacio')
                Dron.Agregar(Altura0)
                mientras leemos altura:
                    valorAltura = leer atributo valor
                    valorLetra = leer altura
                    Altura = Altura(valorAltura, valorLetra)
                    Dron.Agregar(Altura)
                SistemaDrones.Agregar(Dron)
            ListaSistemasDrones.Agregar(SistemaDrones)



Ejecucion de Mensaje:
Recorrer -> instruccion in ListaInstrucciones:
    Recorrer -> dron in SitemaDrones:
    //ESTO REPRESENTA UN SEGUNDO
        Logica de drones.


'''