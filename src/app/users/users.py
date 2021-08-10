from flask import request, jsonify, Blueprint

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def users_regards():
    return jsonify({'message': 'Welcome!'})

@users.route('/user', methods=['POST'])
def create_user():
    from src.main import db
    from src.app.models import User, user_schema
    # Receive requests
    if request.method == 'POST':
        name = request.json['name']
        
        new_user= User(name)

        db.session.add(new_user)
        db.session.commit()
        
        return user_schema.jsonify(new_user)