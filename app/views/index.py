from app import app
from flask import jsonify, url_for, redirect


def root():
    return jsonify({'message': 'Index for testing hehe'}), 201
