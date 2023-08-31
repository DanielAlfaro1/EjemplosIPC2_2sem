'''
    1. Crear sus clases para nodos y listas de la matriz orginal
    (opcional) 2. Crear sus clases para nodos y listas de la matriz de patrones
    3. Crear sus clases para nodos y listas de la matriz reducida
    4. Llenar su matriz original
    5. En base a la matriz original llenar o generar la matriz de patrones (1, 0)
    6. En base a la matriz de patrones, comparar las filas y encontrar patrones iguales
    7. Crear y llenar la matriz reducida, indicando que filas son las que van juntas y sumando sus valores en las "celdas"


    apuntador siguiente
    está en forma de matriz

    diferencias
    la matriz reducida tiene grupos.

Matriz original/matriz de patrones
Tiempos/Amplitud    
         1 2 3
    1   |6|7|0|
    2   |5|8|0|
    3   |0|3|0|
    4   |3|4|0|

         1 2 3
    1   |1|1|0|
    2   |1|1|0|
    3   |0|1|0|
    4   |1|1|0|

    ListaExplorados = Lista()
    Reducida = MatrizRed()
    Patron = None
    for x in range(MatrizOriginal.DevolverTamañoFilas()):
        ExisteEnLista = ListaExplorados.Existe(x+1)
        if ExisteEnLista == False:
            if Patron == None:
                Patron = MatrizOriginal.DevolverPatronFila(x+1) #|0|1|0|

            #Analizar mi matriz comparando el patron
            ListaAuxiliar = Lista()
            ListaAuxiliar.Insertar(x+1)
            ListaExplorados.Insertar(x+1)
            for y in range(MatrizOriginal.DevolverTamañoFilas()):
                if x != y:
                    Existe = MatrizOriginal.CompararPatronFila(y+1, Patron)
                    if Existe == True:
                        ListaAuxiliar.Insertar(y+1)
                        ListaExplorados.Insertar(y+1)
            Reducida.InsertarFila(ListaAuxiliar())

            ListaRecorrido = Reducida.ObtenerUltimoGrupo()
            for x in range(MatrizOriginal.DevolverTamañoColumnas()): #0 1 2
                Auxiliar = ListaRecorrido.Inicio
                Variable = 0
                while Auxiliar != None:    
                    Variable = Variable + MatrizOriginal.ObtenerFilaColumna(Auxiliar.Dato, x+1)
                    Auxiliar = Auxiliar.Siguiente
                Reducida.InsertarUltimaFilaLaColumna(Variable)

            Patron = None

    Grupo1 tiempos=-1, 2, 4-    | | | |
    Grupo2 tiempos=-3-          | | | |

    
                             1   2 3


'''