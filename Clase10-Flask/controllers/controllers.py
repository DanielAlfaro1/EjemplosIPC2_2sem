import xml.etree.ElementTree as ET
from Objeto.ObjetoRandom import ObjetoRandom
import json

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
    for diccionario_hijos in raiz:
        print(diccionario_hijos)
        if diccionario_hijos.tag == 'sentimientos_positivos':
            for Palabras in diccionario_hijos:
                listaPalabras['PalabrasPositivas'].append(Palabras.text.strip())
        if diccionario_hijos.tag == 'sentimientos_negativos':
            for Palabras in diccionario_hijos:
                listaPalabras['PalabrasNegativas'].append(Palabras.text.strip())
    Data = {
        "Codigo":200,
        "Mensaje": "Tu Diccionario ha sido registrado",
        "PalabrasRecibidas": listaPalabras
    }
    print(listaPalabras)
    return(Data)

def Get_Palabras():
    Data = {
        "Codigo":200,
        "Mensaje": "Las palabras ya registradas en el sistema son",
        "PalabrasRegistradas": listaPalabras
    }
    return Data