# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template

from .command import init_app
from .database import init_db, db_session
from .form import DropdownForm
from .views import bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize application
    init_app(app)

    app.register_blueprint(bp)
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app