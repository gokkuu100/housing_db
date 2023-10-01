from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY


db = SQLAlchemy()

class House(db.Model):
    __tablename__ = "houses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Integer, nullable=False)  
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    city = db.Column(db.String(255), nullable=False)
    county = db.Column(db.String(255), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    image_paths = db.Column(db.String, nullable=False)

    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'), nullable=False)
    agent = db.relationship('Agent', back_populates='houses')

    
    users = db.relationship('User', secondary='user_likes', back_populates='liked_houses')

class Agent(db.Model):
    __tablename__ = "agents"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phonebook = db.Column(db.String(255), nullable=False)  
    houses = db.relationship('House', back_populates='agent')

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    phonebook = db.Column(db.String(255), nullable=False)  

    liked_houses = db.relationship('House', secondary='user_likes', back_populates='users')

user_likes = db.Table('user_likes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('house_id', db.Integer, db.ForeignKey('houses.id'), primary_key=True)
)
