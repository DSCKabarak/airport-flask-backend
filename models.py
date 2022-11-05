from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Flight(db.Model):
    __tablename__ = 'flight'

    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('plane.id'))
    airportfrom_id = db.Column(db.Integer, db.ForeignKey('airport.id'))
    airportto_id = db.Column(db.Integer, db.ForeignKey('airport.id'))
    date = db.Column(db.String)

    plane = db.relationship('Plane', back_populates='flight')
    airport_from = db.relationship("Airport", foreign_keys=[airportfrom_id], back_populates='airportfrom')
    airport_to = db.relationship("Airport", foreign_keys=[airportto_id], back_populates='airportto')



class Airport(db.Model):
    __tablename__ = "airport"

    id = db.Column(db.Integer, primary_key=True)
    airportcode = db.Column(db.Integer, nullable=False)
    airportname = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50))

    airportfrom = db.relationship('Flight', foreign_keys=[Flight.airportfrom_id], back_populates='airport_from', cascade='all, delete')
    airportto = db.relationship('Flight', foreign_keys=[Flight.airportto_id], back_populates='airport_to', cascade='all, delete')

    
    def __repr__(self):
        return self.airportcode + " | " + self.airportname


class Plane(db.Model):
    __tablename__ = "plane"

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(5), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    flight = db.relationship('Flight', uselist=False, back_populates='plane')

    def __repr__(self):
        return self.make + " | " + self.model

