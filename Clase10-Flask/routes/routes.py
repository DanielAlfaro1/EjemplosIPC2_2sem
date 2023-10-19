from controllers.controllers import *
from flask import Blueprint, jsonify, Response, request

RutasSaludos = Blueprint("RutasSaludos", __name__)
RutasProyecto = Blueprint("RutasProyecto", __name__)

#Que tipo de métodos existen: GET, POST, PUT, DELETE, etc
@RutasSaludos.route("/SaludoNormal", methods=["GET"])
def SaludoNormal():
    variable = EjecutarunHola()
    print(variable)
    return (jsonify(variable))

@RutasSaludos.route("/SaludoPOST", methods=["POST"])
def SaludoPost():
    print(request.data)
    variable = EjecutarAlgoConXML(request.data)
    print(variable)
    return Response(variable, status=201, mimetype="json")

@RutasSaludos.route("/SaludoPUT", methods=["PUT"])
def SaludoPUT():
    print(request.data)
    variable = EjecutarAlgoConXML(request.data)
    print(variable)
    return Response(variable, status=201, mimetype="json")

@RutasSaludos.route("/SaludParams", methods=["GET"])
def SaludoParams():
    #Obtenemos los parámetros luego del signo ?
    args = request.args
    #Obtenemos un paramétro específico, en este caso "genero"
    print(args.get("genero"))
    variable = EjecutarunHola()
    return (jsonify(variable))

@RutasSaludos.route("/SaludParams2/<genero>/<volumen>", methods=["GET"])
def SaludoParams2(genero, volumen):
    print(genero)
    print(volumen)
    variable = EjecutarunHola()
    return (jsonify(variable))

@RutasProyecto.route("/get-palabras", methods=["GET"])
def ObtenerPalabas():
    Resultado = Get_Palabras()
    return (jsonify(Resultado))

@RutasProyecto.route("/post-archivo-conf", methods=["POST"])
def Archivo_Conf():
    #print(request.data)
    Resultado = Configuracion_Diccionario(request.data)
    return(jsonify(Resultado))
