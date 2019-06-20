import datetime
from app import db, ma


"""Definição da classe dos usuários e seus campos"""
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    posts = db.relationship('Posts', backref='users', lazy=True)
    commentaries = db.relationship('Commentaries', backref='users', lazy=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


"""Definindo o Schema do Marshmallow para facilitar a utilização de JSON"""
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'email', 'password', 'created_on')


user_schema = UsersSchema(strict=True)
users_schema = UsersSchema(strict=True, many=True)
