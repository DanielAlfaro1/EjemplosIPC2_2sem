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