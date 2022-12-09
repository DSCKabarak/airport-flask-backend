
<p align="center">
    <img align="center" src="https://cdn.dribbble.com/users/60166/screenshots/10872300/media/ba277eb11fa7c7b2e3014d0f9a0ada71.jpeg" height="128">
</p>

# Airport Flask Backend Challenge

`💻` This was a challenge to build a simple API driven website using EJS and Flask. This api was built using flask with various tooling.

`🛠️` The tooling used in the project are as follows.
> 
1. `SQLAlchemy & SQlite` - Database ORM and Engine
2. `Flask n' Restful` - API framework and server
3. `flask-redoc` - API documentation using redoc and openapi spec file

## Getting started
Clone the repo and first create a virtual enviroment. The project support python 3

Create a virtual environment by running the following
``` bash
python -m venv venv
```

Then install packages by running following
``` bash
pip install -r requirements.txt
```

Start the application by running following
``` bash
python app.py
```


## Documentation
I used redoc with openapi spec and postman to document the project.

The online documentation is available at this endpoint 
[`challenge/docs`](https://airport-flask-backend.walterbanda.repl.co/docs)

This is a simplified schema of the the various endpoints available

| Airport| Endpoints |
|---------|---------|
| `/airport/${id}` - `DELETE` | ❌ Deletes Airport by given id |
| `/airport/${id}` - `GET` | ✅ GETS Airport by given id |
| `/airport/${id}` - `PUT` | 📝 Updates Airport details of a given id |
| `/airports` - `PUT` | ✅ Get all available Airport details |
| `/airports` - `POST` | 🔧 Create a new airport |

| Plane | Endpoints |
|---------|---------|
| `/plane` - `PUT` | 📝 Updates Plane details |
| `/plane/${id}` - `GET` | ✅ Gets Plane of details of given id |
| `/plane` - `DELETE` | ❌ Deletes Plane of given ID |
| `/planes` - `GET` | ✅ Gets all available Plane details |
| `/planes` - `POST` | 🔧 Creates new Plane details |

| Flight | Endpoints |
|---------|---------|
| `/flight/${id}` - `DELETE` | ❌ Deletes a flight of given ID |
| `/flights` - `GET` | ✅ Gets all available flights |
| `/flights` - `POST` | 🔧 Creates new flight |






## Authors

- [@walterbanda](https://www.github.com/mmurima-kai)

