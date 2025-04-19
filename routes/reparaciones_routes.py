# routes/reparaciones_routes.py

from flask import Blueprint, request, jsonify
from models.reparaciones import Reparacion
from models.db import db
from datetime import datetime

reparaciones = Blueprint('reparaciones', __name__)

# Obtener todas las reparaciones
@reparaciones.route('/api/reparaciones', methods=['GET'])
def get_reparaciones():
    all_reparaciones = Reparacion.query.all()
    return jsonify([r.serialize() for r in all_reparaciones])

# Obtener una reparación por ID
@reparaciones.route('/api/reparaciones/<int:id>', methods=['GET'])
def get_reparacion(id):
    reparacion = Reparacion.query.get(id)
    if not reparacion:
        return jsonify({"message": "Reparación no encontrada"}), 404
    return jsonify(reparacion.serialize())

# Crear una nueva reparación
@reparaciones.route('/api/reparaciones', methods=['POST'])
def add_reparacion():
    data = request.get_json()
    descripcion = data.get("descripcion")
    fecha_ingreso = data.get("fecha_ingreso")
    fecha_entrega = data.get("fecha_entrega")
    estado = data.get("estado")
    vehiculo_id = data.get("vehiculo_id")

    if not all([descripcion, fecha_ingreso, estado, vehiculo_id]):
        return jsonify({"message": "Faltan campos obligatorios"}), 400

    reparacion = Reparacion(
        descripcion=descripcion,
        fecha_ingreso=datetime.strptime(fecha_ingreso, "%Y-%m-%d").date(),
        fecha_entrega=datetime.strptime(fecha_entrega, "%Y-%m-%d").date() if fecha_entrega else None,
        estado=estado,
        vehiculo_id=vehiculo_id
    )

    db.session.add(reparacion)
    db.session.commit()
    return jsonify(reparacion.serialize()), 201

# Actualizar una reparación por ID
@reparaciones.route('/api/reparaciones/<int:id>', methods=['PUT'])
def update_reparacion(id):
    reparacion = Reparacion.query.get(id)
    if not reparacion:
        return jsonify({"message": "Reparación no encontrada"}), 404

    data = request.get_json()
    descripcion = data.get("descripcion")
    fecha_ingreso = data.get("fecha_ingreso")
    fecha_entrega = data.get("fecha_entrega")
    estado = data.get("estado")
    vehiculo_id = data.get("vehiculo_id")

    if descripcion:
        reparacion.descripcion = descripcion
    if fecha_ingreso:
        reparacion.fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d").date()
    if fecha_entrega:
        reparacion.fecha_entrega = datetime.strptime(fecha_entrega, "%Y-%m-%d").date()
    if estado:
        reparacion.estado = estado
    if vehiculo_id:
        reparacion.vehiculo_id = vehiculo_id

    db.session.commit()
    return jsonify(reparacion.serialize())

# Eliminar una reparación por ID
@reparaciones.route('/api/reparaciones/<int:id>', methods=['DELETE'])
def delete_reparacion(id):
    reparacion = Reparacion.query.get(id)
    if not reparacion:
        return jsonify({"message": "Reparación no encontrada"}), 404

    db.session.delete(reparacion)
    db.session.commit()
    return jsonify({"message": "Reparación eliminada con éxito"}), 200
