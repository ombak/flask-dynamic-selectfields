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


# populate database
@click.command('pop-db')
@with_appcontext
def populate_db_command():
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
    click.echo('Populate database.')

# 
def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)
