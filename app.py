from flask import Flask, jsonify, request,redirect
from flask_restful import Resource, Api, marshal_with
from models import db, Airport, Plane, Flight
from schemas import airport, plane, flight
from flask_redoc import Redoc


app = Flask(__name__)
redoc = Redoc(app, "openapi.yaml")

# Database setup & Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


api = Api(app)
db.init_app(app)


# User Pre-Configured details
user = {"username": "admin", "password": "admin123"}

# make sure db migrations is applied
@app.before_first_request
def create_table():
    db.create_all()


# User login
class UserLogin(Resource):

    def post(self):
        data = request.get_json()

        if (
            data["username"] == user["username"]
            and data["password"] == user["password"]
        ):
            return {"message": "logged in"}, 200
        else:
            return {"message": "wrong credentials"}, 404

class Docs(Resource):
  def get(self):
    return redirect("/docs")


class Airports(Resource):
    @marshal_with(airport)
    def get(self):
        airport_objs = Airport.query.all()
        return airport_objs

    @marshal_with(airport)
    def post(self):
        data = request.get_json()

        airport_obj = Airport(**data)

        db.session.add(airport_obj)
        db.session.commit()

        return airport_obj, 201


class Planes(Resource):
    @marshal_with(plane)
    def get(self):
        plane_obj = Plane.query.all()
        return plane_obj

    @marshal_with(plane)
    def post(self):
        data = request.get_json()

        plane_obj = Plane(**data)
        db.session.add(plane_obj)
        db.session.commit()

        return plane_obj, 201


class Flights(Resource):
    @marshal_with(flight)
    def get(self):
        flight_obj = Flight.query.all()

        return flight_obj

    @marshal_with(flight)
    def post(self):
        data = request.get_json()

        flight_obj = Flight(**data)
        db.session.add(flight_obj)
        db.session.commit()

        return flight_obj


class AirportView(Resource):
    @marshal_with(airport)
    def get(self, pk):
        airport_obj = Airport.query.filter_by(id=pk).first()
        if airport_obj:
            return airport_obj
        return {"message": "airport not found"}, 404

    @marshal_with(airport)
    def put(self, pk):
        data = request.get_json()

        airport_obj = Airport.query.filter_by(id=pk).first()

        if "airportcode" in data:
            airport_obj.make = data["airportcode"]
        if "airportname" in data:
            airport_obj.model = data["airportname"]
        if "country" in data:
            airport_obj.year = data["country"]
        db.session.commit()

        return airport_obj

    def delete(self, pk):
        airport_obj = Airport.query.filter_by(id=pk).first()
        if airport_obj:
            db.session.delete(airport_obj)
            db.session.commit()
            airport_objs = Airport.query.all()
            return {"message": "Airport not found"}, 200
        else:
            return {"message": "Airport not found"}, 404


class PlaneView(Resource):
    @marshal_with(plane)
    def get(self, pk):
        plane_obj = Plane.query.filter_by(id=pk).first()
        if plane_obj:
            return plane_obj
        return {"message": "airport not found"}, 404

    @marshal_with(plane)
    def put(self, pk):
        data = request.get_json()

        plane_obj = Plane.query.filter_by(id=pk).first()

        if "make" in data:
            plane_obj.make = data["make"]
        if "model" in data:
            plane_obj.model = data["model"]
        if "year" in data:
            plane_obj.year = data["year"]
        if "capacity" in data:
            plane_obj.capacity = data["capacity"]
        db.session.commit()

        return plane_obj

    @marshal_with(plane)
    def delete(self, pk):
        plane_obj = Plane.query.filter_by(id=pk).first()
        if plane_obj:
            db.session.delete(plane_obj)
            db.session.commit()
            plane_objs = Plane.query.all()
            return plane_objs
        else:
            return {"message": "Plane not found"}, 404


class FlightView(Resource):
    @marshal_with(flight)
    def delete(self, pk):
        flight_obj = Flight.query.filter_by(id=pk).first()

        if flight_obj:
            db.session.delete(flight_obj)
            db.session.commit()

            flight_objs = Flight.query.all()
            return flight_objs

        return {"message": "Flight not found"}, 404

api.add_resource(Docs,'/')
api.add_resource(UserLogin, "/login")
api.add_resource(Airports, "/airports")
api.add_resource(Planes, "/planes")
api.add_resource(Flights, "/flights")
api.add_resource(AirportView, "/airport/<int:pk>")
api.add_resource(PlaneView, "/plane/<int:pk>")
api.add_resource(FlightView, "/flight/<int:pk>")


if __name__ == "__main__":
    app.run(debug=True)
