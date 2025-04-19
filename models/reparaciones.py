# models/reparacion.py

from models.db import db

class Reparacion(db.Model):
    __tablename__ = 'reparaciones'
    
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False)
    fecha_entrega = db.Column(db.Date, nullable=True)
    estado = db.Column(db.String(50), nullable=False)
    vehiculo_id = db.Column(db.Integer, nullable=False)  # No usamos foreign key por tu decisión

    def serialize(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "fecha_ingreso": self.fecha_ingreso.isoformat(),
            "fecha_entrega": self.fecha_entrega.isoformat() if self.fecha_entrega else None,
            "estado": self.estado,
            "vehiculo_id": self.vehiculo_id
        }
