#estudiantes -> Atributos:Nombre, edad, carnet, promedio
#estudiantes -> Metodos/acciones: Estudiar, aprender, aprobar, inscribrse, resolver
#cursos -> Atributos: Nombre, creditos, profesor, hora, listaEstudiantes
#cursos -> Metodos/acciones: DejarTarea, RealizarExamen, MostrarContenido, AsignarAlumnos
#horarios -> Atributos: jornada, dia, duracion, rotativo
#horarios -> Metodos/acciones: DefinirHoras, IniciarPeriodo, Agregarcurso, ClasificarJornada


#En comun: medios de transporte, asiento, ruedas, velocidad, no. pasajeros, chofer, peso, no. ruedas, tamaño, medio de tranposrte
#bicicleta: no tiene motor, no contamina, cadena, manubrio
#moto: tanque de combustible, cadena, retrovisores, cilindraje, manubrio
#carro: tanque de combustible, retrovisores, cilindraje, timon
#tren: controles, vagones, tipo-combustible, estaciones

#clase: medios_transporte
#clases hijas: automovil, motocicleta, bicicleta, tren

#objeto tipo tren: 3 vagones, carbon
#objeto tipo tren: 5 vagones, electrico

class bicicleta:
    def __init__(self):
        self.manubrio = ''
        self.cadena = ''
        self.pedales = ''
        self.color = ''
        self.marca = ''
        self.No_ruedas = ''
        self.No_pasajeros = ''
        self.No_asientos = ''
        self.Frenos = ''
    
    def manejarse(self):
        print("se maneja")
    
    def girar(self, direccion):
        print("gira a la "+direccion)

    def Avanzar(self):
        print("Se pedalea")

class Automovil:
    def __init__(self):
        self.Color = ''
        self.Cilindraje = ''
        self.No_Asientos = ''
        self.No_Pasajeros = ''
        self.Marca = ''
        self.Acelerador = ''
        self.Frenos = ''
        self.No_Puertas = ''

    def manejarse(self):
        print("Se maneja")
    
    def AbirPuerta(self, No_Puerta):
        print("Se abre puerta "+str(No_Puerta))
    
    def girar(self, direccion):
        print("gira a la "+direccion)

    def Avanzar(self):
        print("Se acelera")

CarroDeportivo = Automovil()#Color rojo, 2 puertas
CarroFamiliar = Automovil()#Color blanco, 4 puertas
BicicletaDeporte = bicicleta()#Color amarillo, cadena de acero
BicicletaMontaña = bicicleta()#Color verded, cadena de aluminio

CarroDeportivo.girar("derecha")
CarroDeportivo.Avanzar()

BicicletaDeporte.girar("Izquierda")
BicicletaMontaña.Avanzar()