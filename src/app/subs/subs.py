from flask import request, jsonify, Blueprint
from sqlalchemy import insert

subs = Blueprint('subs', __name__)

@subs.route('/subs', methods=['GET'])
def users_regards():
    return jsonify({'message': 'Welcome!'})

@subs.route('/sub', methods=['GET','POST'])
def create_sub():
    from src.app.models import Channel
    from src.app.models import User
    from src.main import db

    # Receive requests
    if request.method == 'POST':
        user_id = request.json['user_id']
        channel_id = request.json['channel_id']

        user = User.query.filter_by(user_id=user_id).first()
        channel = Channel.query.filter_by(channel_id=channel_id).first()

        channel.subscribers.append(user)
        db.session.commit()

        return jsonify({'message': 'You are subscribed!'})
        
        # from sqlalchemy import create_engine
        # my_conn = create_engine("mysql+pymysql://root:root@db/youtube")

        # query = "INSERT INTO  `youtube`.`subs` (`user_id` ,`channel_id`) VALUES(%s,%s)"
        # my_data = (user_id, channel_id)
            
        # id = my_conn.execute(query, my_data)
        # print(id)

        # return jsonify({'message': 'You are subscribed!'})