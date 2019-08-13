# -*- coding: utf-8 -*-
import click
from flask.cli import with_appcontext
from .database import init_db, db_session
from .models import Car, Model, Version


@click.command('init-db')
@with_appcontext
def init_db_command():
    """initialize database"""
    init_db()
    click.echo('Initialized the database.')


def populate_car():
    cars = [Car('Aston Martin'), 
        Car('Audi'),
        Car('BMW'),
        Car('Cadillac'),
        Car('Chevrolet'),
        Car('Datsun'),
        Car('Ferrari'),
        Car('Ford')]
    db_session.add_all(cars)
    db_session.commit()

def get_cars(id):
    return Car.query.get(id)

def populate_model():
    models = [Model(get_cars(1), 'DB5'),
        Model(get_cars(1), 'Rapide'),
        Model(get_cars(1), 'Lagonda'),
        Model(get_cars(1), 'V8 Vantage'),
        Model(get_cars(1), 'DBS'),
        Model(get_cars(2), 'Audi 50'),
        Model(get_cars(2), 'Audi F103'),
        Model(get_cars(2), 'Audi 80'),
        Model(get_cars(2), 'Audi 90'),
        Model(get_cars(2), 'Audi 100'),
        Model(get_cars(2), 'Audi 200'),
        Model(get_cars(3), 'BMW F650GS'),
        Model(get_cars(3), 'BMW F800GS'),
        Model(get_cars(3), 'BMW F800R'),
        Model(get_cars(3), 'BMW G450X'),
        Model(get_cars(3), 'BMW R1200GR')]
    db_session.add_all(models)
    db_session.commit()

def get_models(id):
    return Model.query.get(id)

def populate_version():
    versions = [Version(get_models(1), 'DB5 Vantage'),
        Version(get_models(1), 'DB5 convertible'),
        Version(get_models(1), 'DB5 shooting-brake'),
        Version(get_models(2), 'Rapide S 2013'),
        Version(get_models(2), 'RapideE'),
        Version(get_models(2), 'Rapide AMR'),
        Version(get_models(3), 'Series 1 1974-1975'),
        Version(get_models(3), 'Series 2 1976-1985'),
        Version(get_models(6), 'Typ 86'),
        Version(get_models(12), '2008-2016')]
        
    db_session.add_all(versions)
    db_session.commit()

# populate database
@click.command('pop-db')
@with_appcontext
def populate_db_command():
    populate_car()
    populate_model()
    populate_version()
    click.echo('Populate database.')

# 
def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)
