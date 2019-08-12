# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    models = relationship("Model", back_populates="cars") # relationship
    orders = relationship("Order", back_populates="cars")

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Car %r>' % self.name

    @property 
    def serializable(self):
        return {'id':self.id, 'name':self.name}
    
    
class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    model = Column(String(128), nullable=False)
    cars = relationship("Car", back_populates="models") # relationship
    versions = relationship("Version", back_populates="models") # relationship
    orders = relationship("Order", back_populates="models")

    def __init__(self, cars=None, model=None):
        self.cars = cars
        self.model = model

    def __repr__(self):
        return '<Model %r>' % self.model
    
    @property
    def serializable(self):
        return {'id':self.id, 'car_id':self.car_id, 'model':self.model}


class Version(Base):
    __tablename__ = 'versions'
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('models.id'), nullable=False)
    version = Column(String(128), nullable=False) 
    models = relationship("Model", back_populates="versions") # relationship
    orders = relationship("Order", back_populates="versions")

    def __init__(self, models=None, version=None):
        self.models = models
        self.version = version

    def __repr__(self):
        return '<Version %r>' % self.version
    
    @property
    def serializable(self):
        return {'id':self.id, 
                'model_id':self.model_id, 
                'version':self.version}


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    model_id = Column(Integer, ForeignKey('models.id'), nullable=False)
    version_id = Column(Integer, ForeignKey('versions.id'), nullable=False)
    customer_name = Column(String(128), nullable=False)
    cars = relationship("Car", back_populates="orders")
    models = relationship("Model", back_populates="orders")
    versions = relationship("Version", back_populates="orders")

    def __init__(self, cars, models, versions, customer_name):
        self.cars = cars
        self.models = models
        self.versions = versions
        self.customer_name = customer_name
    
    def __repr__(self):
        return '<Order %r>' % self.customer_name
    
    def serializable(self):
        return {'id':self.id, 
                'car_id':self.car_id, 
                'model_id':self.model_id, 
                'version_id':self.version_id, 
                'customer_name':self.customer_name}