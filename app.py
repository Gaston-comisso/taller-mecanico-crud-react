from flask import Flask, jsonify
from config.config import DATABASE_CONNECTION_URI
from routes.client_routes import client
from routes.vehiculos_routes import vehiculos
from routes.reparaciones_routes import reparaciones
from models.db import db

app = Flask(__name__)

# Registra los blueprints
app.register_blueprint(reparaciones)
app.register_blueprint(client)
app.register_blueprint(vehiculos)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la base de datos
db.init_app(app)

# Configurar los encabezados de CORS manualmente
@app.after_request
def apply_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:5173"  # Permite el origen de tu frontend
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"  # Permite cabeceras
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"  # Permite métodos
    return response

# Inicializa las tablas de la base de datos
with app.app_context():
    from models.client import Client
    from models.vehiculo import Vehiculo  
    from models.reparaciones import Reparacion
    db.create_all()

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
