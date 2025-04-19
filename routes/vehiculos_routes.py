from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from models.db import db
from models.vehiculo import Vehiculo  # Asegúrate de importar el modelo Vehiculo

vehiculos = Blueprint('vehiculo', __name__)

# Obtener todos los vehículos
from flask import jsonify
from models.vehiculo import Vehiculo

# Obtener todos los vehículos
@vehiculos.route('/api/vehiculo')
def get_vehiculo():
    marca = request.args.get('marca')  # Captura el parámetro de la URL

    query = Vehiculo.query
    if marca:
        query = query.filter(Vehiculo.marca.ilike(f"%{marca}%"))  # Búsqueda flexible

    vehiculos = query.all()

    if not vehiculos:
        return jsonify({"message": "No se encontraron vehículos"}), 404

    return jsonify([vehiculo.serialize() for vehiculo in vehiculos])

# Agregar un nuevo vehículo
@vehiculos.route('/api/add_vehiculo', methods=['POST'])
def add_vehiculo():
    data = request.get_json()

    if not data or not all(key in data for key in ['marca', 'modelo', 'patente', 'año']):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    try:
        print(f"Datos recibidos: {data}")  # Ver qué datos llegan

        new_vehiculo = Vehiculo(
            marca=data['marca'],
            modelo=data['modelo'],
            patente=data['patente'],
            año=data['año']
        )
        print(f"Creando vehículo: {new_vehiculo.marca}, {new_vehiculo.modelo}, {new_vehiculo.patente}, {new_vehiculo.año}")

        db.session.add(new_vehiculo)
        db.session.commit()

        return jsonify({'message': 'Vehículo agregado exitosamente', 'vehiculo': new_vehiculo.serialize()}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'El vehículo ya existe con esa patente'}), 400

    except Exception as e:
        db.session.rollback()
        print(f"Error inesperado: {e}")  # Ver el error en la terminal
        return jsonify({'error': 'Error al agregar el vehículo'}), 500

# Eliminar un vehículo
@vehiculos.route("/api/del_vehiculo/<int:id>", methods=['DELETE'])
def delete_vehiculo(id):
    vehiculo = Vehiculo.query.get(id)  # Busca el vehículo por su id

    if not vehiculo:
        return jsonify({'message': 'Vehículo no encontrado'}), 404

    try:
        db.session.delete(vehiculo)  # Elimina el vehículo de la base de datos
        db.session.commit()
        return jsonify({'message': 'Vehículo eliminado exitosamente'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Actualizar un vehículo
@vehiculos.route('/api/up_vehiculo/<int:id>', methods=['PUT'])
def update_vehiculo(id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No se recibieron datos'}), 400

    vehiculo = Vehiculo.query.get(id)  # Busca el vehículo por su id

    if not vehiculo:
        return jsonify({'error': 'Vehículo no encontrado'}), 404

    try:
        if "marca" in data:
            vehiculo.marca = data['marca']
        if 'modelo' in data:
            vehiculo.modelo = data['modelo']
        if 'patente' in data:
            vehiculo.patente = data['patente']
        if 'año' in data:
            vehiculo.año = data['año']

        db.session.commit()  # Realiza el commit de la actualización

        return jsonify({'message': 'Vehículo actualizado correctamente', 'vehiculo': vehiculo.serialize()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Actualizar parcialmente un vehículo
@vehiculos.route('/api/update_vehiculo/<int:id>', methods=['PATCH'])
def patch_vehiculo(id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No se recibieron datos'}), 400

    vehiculo = Vehiculo.query.get(id)  # Busca el vehículo por su id

    if not vehiculo:
        return jsonify({'error': 'Vehículo no encontrado'}), 404

    try:
        if 'marca' in data and data['marca']:
            vehiculo.marca = data['marca']
        if 'modelo' in data and data['modelo']:
            vehiculo.modelo = data['modelo']
        if 'patente' in data and data['patente']:
            vehiculo.patente = data['patente']
        if 'año' in data and data['año']:
            vehiculo.año = data['año']

        db.session.commit()  # Realiza el commit de la actualización

        return jsonify({'message': 'Vehículo actualizado correctamente', 'vehiculo': vehiculo.serialize()}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
