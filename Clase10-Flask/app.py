from flask import Flask
from routes.routes import RutasSaludos

app = Flask(__name__)
app.register_blueprint(RutasSaludos)