import os
import sys
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

# children = relationship("Child", back_populates="parent")
# parent = relationship("Parent", back_populates="children")

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(Date, nullable=False)
    
    favorites = relationship("Favorite", back_populates="user")
    # children = relationship("Child", back_populates="parent")
    
class Planets(Base):
    __tablename__ = 'planets'
    planetID = Column(Integer, primary_key=True)
    planetName = Column(String(50), nullable=False, unique=True)
    population = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    
    characters = relationship("Character", back_populates="planets")
    favorites = relationship("Favorite", back_populates="planets")
    
class Character(Base):
    __tablename__ = 'character'
    characterID = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    species = Column(String(50), nullable=False, unique=True)
    homeworld = Column(Integer, ForeignKey(Planets.planetID))
    
    favorites = relationship("Favorite", back_populates="character")
    planets = relationship("Planets", back_populates="character")
    
class Vehicles(Base):
    __tablename__ = 'vehicle'
    vehicleID = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    type = Column(String(50), nullable=False)
    owner = Column(Integer, ForeignKey(Character.characterID))
    
    favorites = relationship("Favorite", back_populates="vehicle")
    characters = relationship("Character", back_populates="vehicle")
       
class Favorites(Base):
    __tablename__ = 'favorites'
    favorites_id = Column(Integer, primary_key=True)
    user_id =  Column(Integer, ForeignKey(User.id))
    character_id = Column(Integer, ForeignKey(Character.characterID))
    planet_id = Column(Integer, ForeignKey(Planets.planetID))
    vehicles_id = Column(Integer, ForeignKey(Vehicles.vehicleID))
    
    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planets = relationship("Planets", back_populates="favorites")
    vehicle = relationship("Vehicles", back_populates="favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
