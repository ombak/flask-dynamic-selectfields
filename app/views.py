# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify, request, jsonify
from .form import OrderForm
from .models import Car, Model, Version


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = OrderForm()
    return render_template('index.html', form=form)


"""load ajax
"""
@bp.route('/_load_cars', methods=['GET', 'POST'])
def load_cars():
    cars = Car.query.all()
    return jsonify(data = [c.serializable for c in cars])

@bp.route('/_load_models')
def load_models():
    car_id = request.args.get('car_id', 0, type=int)
    models = Model.query.filter(Model.car_id == car_id).all()
    return jsonify(data = [m.serializable for m in models])

@bp.route('/_load_versions')
def load_versions():
    pass