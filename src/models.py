import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('favoritos.usuario_id'))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(250))
    diameter = Column(Integer)
    terrain = Column(String(250), nullable=False)
   
    

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    manufacturer = Column(String(250))
    model = Column(String(250))
    hyperdrive_rating = Column(Integer)
   
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    mass = Column(Integer)
    hair_color = Column(String(250))
    birth_year = Column(String(250))
   

class favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planetas = relationship("Planets")
    naves_estelares = relationship("Starships")
    personas = relationship("People")
    



    


  


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
