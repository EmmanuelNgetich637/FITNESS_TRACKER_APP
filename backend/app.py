from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

#Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

#Use environment variable for DB with fallback
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Import routes (register blueprints)
from routes.user_routes import user_bp
from routes.workout_routes import workout.BrokenPipeError

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(workout_bp, url_prefix='/workouts')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)