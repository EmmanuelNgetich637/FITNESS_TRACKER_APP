from flask import Blueprint, request, jsonify
from models import User, Workout
from extensions import db


workout_bp = Blueprint('workout_bp', __name__)

@workout_bp.route('/<int:user_id>', methods=['POST'])
def add_workout(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.json
    required_fields = ['activity', 'duration']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    workout = Workout(
        activity=data['activity'],
        duration=data['duration'],
        user_id=user_id
    )
    db.session.add(workout)
    db.session.commit()
    return jsonify(workout.to_dict()), 201

@workout_bp.route('/<int:user_id>', methods=['GET'])
def get_workouts(user_id):
    user = User.query.get(user_id)  # fixed typo here
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    workouts = Workout.query.filter_by(user_id=user_id).all()
    return jsonify([w.to_dict() for w in workouts])
