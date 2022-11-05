from flask_restful import fields

# Serializers
airport = {
    "id": fields.Integer,
    "airportcode": fields.String,
    "airportname": fields.String,
    "country": fields.String
}

plane = {
    "id": fields.Integer,
    "make": fields.String,
    "model": fields.String,
    "year": fields.String,
    "capacity": fields.Integer
}

flight = {
    "id": fields.Integer,
    "plane_id": fields.Integer,
    "airportfrom_id": fields.Integer,
    "airportto_id": fields.Integer,
    "date": fields.String
}