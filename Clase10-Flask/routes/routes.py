from controllers.controllers import *
from flask import Blueprint, jsonify, Response, request

RutasSaludos = Blueprint("RutasSaludos", __name__)

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