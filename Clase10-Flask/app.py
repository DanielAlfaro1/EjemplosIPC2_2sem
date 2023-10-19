from flask import Flask
from routes.routes import RutasSaludos, RutasProyecto

app = Flask(__name__)
app.register_blueprint(RutasSaludos)
app.register_blueprint(RutasProyecto)