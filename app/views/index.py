from app import app
from flask import request as req, jsonify, url_for, redirect



def index():
    return jsonify({'message': 'Index for testing hehe'}), 201


def index_redirect():
    return redirect(url_for('index')), 301
