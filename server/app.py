#!/usr/bin/env python3

from flask import Flask, request, session, jsonify
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError

from models import db, User, Recipe

# Flask app configuration
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Initialize extensions
CORS(app)
bcrypt = Bcrypt(app)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# SIGNUP
class Signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {'errors': ['Username and password are required.']}, 422

        try:
            user = User(
                username=username,
                image_url=data.get('image_url'),
                bio=data.get('bio')
            )
            user.password_hash = password
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return user.to_dict(), 201
        except Exception as e:
            return {'errors': [str(e)]}, 422

# AUTO-LOGIN CHECK
class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            if user:
                return user.to_dict(), 200
        return {'error': 'Unauthorized'}, 401

# LOGIN
class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()

        if user and user.authenticate(data['password']):
            session['user_id'] = user.id
            return user.to_dict(), 200
        return {'error': 'Invalid credentials'}, 401

# LOGOUT
class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session.pop('user_id')
            return {}, 204
        return {'error': 'Unauthorized'}, 401

# RECIPE INDEX
class RecipeIndex(Resource):
    def get(self):
        if not session.get('user_id'):
            return {'error': 'Unauthorized'}, 401
        recipes = [recipe.to_dict() for recipe in Recipe.query.all()]
        return recipes, 200

    def post(self):
        if not session.get('user_id'):
            return {'error': 'Unauthorized'}, 401

        data = request.get_json()
        try:
            new_recipe = Recipe(
                title=data['title'],
                instructions=data['instructions'],
                minutes_to_complete=data['minutes_to_complete'],
                user_id=session['user_id']
            )
            db.session.add(new_recipe)
            db.session.commit()
            return new_recipe.to_dict(), 201
        except (ValueError, IntegrityError) as e:
            return {'error': str(e)}, 422

# Add resources to the API
api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(RecipeIndex, '/recipes')

# Run the application
if __name__ == '__main__':
    app.run(port=5555, debug=True)
