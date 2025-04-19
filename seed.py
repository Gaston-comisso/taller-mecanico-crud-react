import os
import json
from app import app
from models.db import db
from models.client import Client
from models.vehiculo import Vehiculo
from models.reparaciones import Reparacion  # Importamos el modelo Reparacion

DATA_DIR = 'data'

def populate_clients(data):
    created = 0
    for item in data:
        name = item.get('name')
        email = item.get('email')
        phone = item.get('phone')

        if not name or not email or not phone:
            continue

        exists = Client.query.filter(
            (Client.email == email) | (Client.phone == phone)
        ).first()

        if exists:
            continue

        client = Client(name=name, email=email, phone=phone)
        db.session.add(client)
        created += 1

    return created

def populate_vehiculos(data):
    created = 0
    for item in data:
        marca = item.get('marca')
        modelo = item.get('modelo')
        patente = item.get('patente')
        año = item.get('año')  # Usamos "año", tal cual como en tu JSON

        if not marca or not modelo or not patente or not año:
            continue

        exists = Vehiculo.query.filter(Vehiculo.patente == patente).first()
        if exists:
            continue

        vehiculo = Vehiculo(marca=marca, modelo=modelo, patente=patente, año=año)
        db.session.add(vehiculo)
        created += 1

    return created

def populate_reparaciones(data):  # Función para poblar reparaciones
    created = 0
    for item in data:
        descripcion = item.get('descripcion')
        fecha_ingreso = item.get('fecha_ingreso')
        fecha_entrega = item.get('fecha_entrega')
        estado = item.get('estado')
        vehiculo_id = item.get('vehiculo_id')

        if not descripcion or not fecha_ingreso or not estado or not vehiculo_id:
            continue

        reparacion = Reparacion(
            descripcion=descripcion,
            fecha_ingreso=fecha_ingreso,
            fecha_entrega=fecha_entrega if fecha_entrega else None,
            estado=estado,
            vehiculo_id=vehiculo_id
        )
        db.session.add(reparacion)
        created += 1

    return created

def populate_all():
    with app.app_context():
        print("Entrando en el contexto de la app...")
        for filename in os.listdir(DATA_DIR):
            print(f"Revisando archivo: {filename}")
            if not filename.endswith('.json'):
                print(f"Archivo ignorado: {filename}")
                continue

            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)

            print(f"Datos cargados desde {filename}: {data}")

            if 'clients' in filename:
                created = populate_clients(data)
                print(f'{created} clientes cargados desde {filename}')
            elif 'vehiculos' in filename:
                created = populate_vehiculos(data)
                print(f'{created} vehículos cargados desde {filename}')
            elif 'reparaciones' in filename:  # Agregamos la condición para reparaciones
                created = populate_reparaciones(data)
                print(f'{created} reparaciones cargadas desde {filename}')
            else:
                print(f'Se ignoró el archivo {filename}, tipo desconocido.')

        print("Haciendo commit a la base de datos...")
        db.session.commit()

if __name__ == '__main__':
    populate_all()
