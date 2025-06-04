from flask import Blueprint, request, jsonify
from models import User
from extensions import db


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'username already exists'}), 409
    
    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])