# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify, request, jsonify
from .form import OrderForm
from .models import Car, Model, Version


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/add_orders', methods=['GET', 'POST'])
def add_orders():
    form = OrderForm()
    return render_template('add_order.html', title="Add Orders", form=form)


"""load ajax
"""
@bp.route('/_load_cars', methods=['GET'])
def load_cars():
    try:
        cars = Car.query.all()
        return jsonify(status=True, data=[c.serializable for c in cars])
    except:
        return jsonify(status=False)

@bp.route('/_load_models', methods=['GET'])
def load_models():
    car_id = request.args.get('car_id', 0, type=int)
    try:
        models = Model.query.filter(Model.car_id == car_id).all()
        return jsonify(status=True, data=[m.serializable for m in models])
    except:
        return jsonify(status=False)

@bp.route('/_load_versions', methods=['GET'])
def load_versions():
    model_id = request.args.get('model_id', 0, type=int)
    try:
        versions = Version.query.filter(Version.model_id == model_id).all()
        return jsonify(status=True, data=[v.serializable for v in versions])
    except:
        return jsonify(status=False)
