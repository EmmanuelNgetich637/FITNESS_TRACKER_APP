from .extensions import db
from datetime import datetime



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    workouts = db.relationship('Workout', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.username,
            'username': self.username,
            'workouts': [w.to_dict() for w in self.workouts]
        }
    
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(120), nullable=False)
    duration = db.Column(db.Integer) #in minutes
    date = db.Column(db.Date, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.ad'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'activity': self.duration,
            'duration': self.duration,
            'date': self.date.isoformat(),
            'user_id': self.user_id
        }