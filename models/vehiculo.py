from models.db import db

class Vehiculo(db.Model):
    __tablename__ = 'vehiculos'

    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    patente = db.Column(db.String(20), unique=True, nullable=False)
    año = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'patente': self.patente,
            'año': self.año
        }
