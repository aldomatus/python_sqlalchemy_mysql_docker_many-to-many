from src.main import db, ma

#---------Models--------------------------

subs = db.Table('subs',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.Column('channel_id', db.Integer, db.ForeignKey('channels.channel_id'))
)

#------------User Model-----------------
class User(db.Model):
    __tablename__= 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    subscriptions = db.relationship('Channel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "name")

user_schema = UserSchema()
users_schema = UserSchema(many = True)

#------------Channel Model-----------------
class Channel(db.Model):
    __tablename__= 'channels'
    channel_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name

class ChannelSchema(ma.Schema):
    class Meta:
        fields = ("channel_id", "name")

channel_schema = ChannelSchema()
channels_schema = ChannelSchema(many = True)

db.create_all()