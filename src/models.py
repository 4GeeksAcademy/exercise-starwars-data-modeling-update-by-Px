import os
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from eralchemy2 import render_er

db = SQLAlchemy()  # Correct declaration before the classes

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    email = db.Column(String, nullable=False, unique=True)
    password = db.Column(String, nullable=False)
    created_at = db.Column(String, nullable=False)

    favorites = relationship("Favorite", back_populates="user")

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String)
    gender = db.Column(db.String)
    height = db.Column(db.String)
    mass = db.Column(db.String)

    favorites = relationship("Favorite", back_populates="character")

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String, nullable=False)
    climate = db.Column(String)
    terrain = db.Column(String)
    population = db.Column(String)

    favorites = relationship("Favorite", back_populates="planet")

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = db.Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = db.Column(Integer, ForeignKey('planet.id'), nullable=True)

    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")

# Only generate the diagram manually when necessary
# render_er(db.Model.metadata, 'diagram.png')
