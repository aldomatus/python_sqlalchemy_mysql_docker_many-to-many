from flask import request, jsonify, Blueprint

channels = Blueprint('channels', __name__)

@channels.route('/channels', methods=['GET'])
def users_regards():
    return jsonify({'message': 'Welcome!'})

@channels.route('/channel', methods=['POST'])
def create_user():
    from src.main import db
    from src.app.models import Channel, channel_schema
    # Receive requests
    if request.method == 'POST':
        name = request.json['name']

        new_channel= Channel(name)

        db.session.add(new_channel)
        db.session.commit()
        
        return channel_schema.jsonify(new_channel)