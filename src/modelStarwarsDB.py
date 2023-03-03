import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(50), nullable=False)

class Favourites(Base):
    __tablename__ = 'favourites'
    favourite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    starship_id = Column(Integer, ForeignKey('starships.starship_id'))

class Characters(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.planet_id'))
    gender = Column(String(10))
    hairColor = Column(String(250))
    skinColor = Column(String(250))
    eyeColor = Column(String(250))

class Planets(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250))
    climate = Column(String(250))
    population = Column(Integer)
    diameter = Column(Integer)

class Starships(Base):
    __tablename__ = 'starships'
    starship_id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    pilot_id = Column(Integer, ForeignKey('characters.character_id'))
    model = Column(String(500))
    manufacturer = Column(String(250))
    cost = Column(Integer)
    topSpeed = Column(Integer)
    maxCargo = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagramStarwars.png')
