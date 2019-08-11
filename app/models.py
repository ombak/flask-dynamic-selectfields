# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    models = relationship("Model", back_populates="cars") # relationship

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Car %r>' % self.name
    

class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    model = Column(String(128), nullable=False)
    cars = relationship("Car", back_populates="models") # relationship
    versions = relationship("Version", back_populates="models") # relationship

    def __init__(self, cars=None, model=None):
        self.cars = cars
        self.model = model

    def __repr__(self):
        return '<Model %r>' % self.model


class Version(Base):
    __tablename__ = 'versions'
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('models.id'), nullable=False)
    version = Column(String(128), nullable=False) 
    models = relationship("Model", back_populates="versions") # relationship

    def __init__(self, models=None, version=None):
        self.models = models
        self.version = version

    def __repr__(self):
        return '<Version %r>' % self.versions