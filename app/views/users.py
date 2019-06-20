from app import app, db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema


@app.route('/v1/users', methods=['GET'])
def get_users():
    users = Users.query.all()

    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'successfully fetched', 'data': result.data})

    return jsonify({'message': 'nothing found', 'data': []})



@app.route('/v1/users', methods=['POST'])
def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    user = Users(username, password, name, email)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.jsonify(user)
        return jsonify({'message': 'unable to create', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': []}), 500