import xml.etree.ElementTree as ET
from Objeto.ObjetoRandom import ObjetoRandom
import json
from Objeto.Diccionario import Diccionario

listaPalabras = {
    'PalabrasPositivas' : [],
    'PalabrasNegativas' : []
}

def EjecutarunHola():
    print("Hola mundo soy un hola en consola")
    return(
        '''{
        "Codigo":200,
        "Mensaje": "Hola mundo, soy un hola en servidor"
        }''')

def EjecutarAlgoConXML(Parametros):
    nombre = ""
    curso = ""
    numero = ObjetoRandom()
    if Parametros != None:
        root = ET.fromstring(Parametros)
        for hijo in root:
            for hijoDatos in hijo:
                if hijoDatos.tag == 'Nombre':
                    nombre = hijoDatos.text
                elif hijoDatos.tag == 'Curso':
                    curso = hijoDatos.text
    return(
        '''{
        "Codigo":200,
        "Mensaje": "Hola '''+nombre+''', Tu curso es: '''+curso+''' Tu numero random es:'''+str(numero.Numero)+'''"
        }''')

def Configuracion_Diccionario(Parametros):
    params = Parametros.decode('utf-8')
    params = json.loads(params)
    raiz = ET.fromstring(params['Diccionario'])
    MiDiccionario = Diccionario()
    MiDiccionario.CargarNuevasPalabras(raiz)
    MiDiccionario.GuardarDiccionario()
    Data = {
        "Codigo":200,
        "Mensaje": "Tu Diccionario ha sido registrado",
        "PalabrasRecibidas": MiDiccionario.ObtenerPalbrasJSON()
    }
    print(MiDiccionario.ObtenerPalbrasJSON())
    return(Data)

def Get_Palabras():
    MiDiccionario = Diccionario()
    Data = {
        "Codigo":200,
        "Mensaje": "Las palabras ya registradas en el sistema son",
        "PalabrasRegistradas": MiDiccionario.ObtenerPalbrasJSON()
    }
    return Data

def ReinciarDiccionario():
    MiDiccionario = Diccionario()
    MiDiccionario.Reiniciar()
    Data = {
        "Codigo":200,
        "Mensaje": "Las palabras ya registradas en el sistema son",
        "PalabrasRegistradas": MiDiccionario.ObtenerPalbrasJSON()
    }
    return Data

def LecturaFecha(Parametros):
    #Guatemala, 15/01/2023 15:25 hrs.
    params = Parametros.decode('utf-8')
    params = json.loads(params)
    Fecha = params['Fecha']
    print(Fecha)
    Fecha = Fecha.split("Guatemala, ")[1]
    print(Fecha)
    Fecha = Fecha.split(" ")[0]
    print(Fecha)
    Fecha = Fecha.split("/")
    Dia = Fecha[0]
    Mes = Fecha[1]
    Anio = Fecha[2]
    print(Dia, Mes, Anio)
    Fecha_Inferior = params['FechaInf']
    Fecha_Inferior = Fecha_Inferior.split("/")
    Dia_Inferior = Fecha_Inferior[0]
    Mes_Inferior = Fecha_Inferior[1]
    Anio_Inferior = Fecha_Inferior[2]
    Fecha_Superior = params['FechaSup']
    Fecha_Superior = Fecha_Superior.split("/")
    Dia_Superior = Fecha_Superior[0]
    Mes_Superior = Fecha_Superior[1]
    Anio_Superior = Fecha_Superior[2]

    #Buscar en base de datos todos los mensajes
    bandera = False
    bandera2 = False
    ListaMensajesFiltro = []
    
    for mensaje in RAIZXMLMensajes:
        for elemento in mensaje:
            #METODO 1
            if elemento.tag == "Fecha":
                FechaMensaje = elemento.text
                FechaMensaje = FechaMensaje.split("/")
                if FechaMensaje[2] >= int(Anio_Inferior) and FechaMensaje[2] <= int(Anio_Superior):
                    if FechaMensaje[1] >= int(Mes_Inferior) and FechaMensaje[1] <= int(Mes_Superior):
                        if FechaMensaje[0] >= int(Dia_Inferior) and FechaMensaje[0] <= int(Dia_Superior):
                            ListaMensajesFiltro.append(mensaje)

            #METODO 2
            if elemento.tag == "Anio":
                if int(elemento.text) >= int(Anio_Inferior) and int(elemento.text) <= int(Anio_Superior):
                    bandera = True
            if bandera == True and elemento.tag == "Mes":
                if int(elemento.text) >= int(Mes_Inferior) and int(elemento.text) <= int(Mes_Superior):
                    bandera2 = True
                else:
                    bandera = False
            if bandera2 == True and elemento.tag == "Dia":
                if int(elemento.text) >= int(Dia_Inferior) and int(elemento.text) <= int(Dia_Superior):
                    ListaMensajesFiltro.append(mensaje)
                bandera = False
                bandera2 = False


    return "hola"