from app import app
from flask import request as req, jsonify, url_for, redirect
from ..models.users import Users
from datetime import datetime



@app.route('/v1', methods=['GET'])
def index():
    return jsonify({'message': 'Index for testing hehe'}), 201

@app.route('/', methods=['GET'])
def index_redirect():
    return redirect(url_for('index')), 301
