import xml.etree.ElementTree as ET
from Objeto.ObjetoRandom import ObjetoRandom

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