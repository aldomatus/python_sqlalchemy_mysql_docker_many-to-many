# Flask libraries
from src.app import create_app
from flask import Flask, blueprints, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = create_app()

# ------------Registro de los blueprints----
from src.app.users.users import users
from src.app.channels.channels import channels
from src.app.subs.subs import subs

app.register_blueprint(users)
app.register_blueprint(channels)
app.register_blueprint(subs)

#--------Instances SQLALchemy and Marshmallow---------
db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello World'})


# https://stackoverflow.com/questions/58391835/flask-marshmallow-serialize-many-to-many-relation-with-extra-field
# https://stackoverflow.com/questions/63203540/many-to-many-relationship-flask-sqlalchemy-and-marshmallow