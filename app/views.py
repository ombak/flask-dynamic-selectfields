# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify, request, jsonify
from .form import OrderForm
from .database import db_session
from .models import Car, Model, Version, Order

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/add_orders', methods=['GET'])
def add_orders():
    form = OrderForm()
    return render_template('add_order.html', title="Add Orders", form=form)


"""load ajax
"""
@bp.route('/_load_cars', methods=['GET'])
def load_cars():
    try:
        cars = Car.query.all()
        return jsonify(success=True, data=[c.serializable for c in cars])
    except:
        return jsonify(success=False)

@bp.route('/_load_models', methods=['GET'])
def load_models():
    car_id = request.args.get('car_id', 0, type=int)
    try:
        models = Model.query.filter(Model.car_id == car_id).all()
        return jsonify(success=True, data=[m.serializable for m in models])
    except:
        return jsonify(success=False)

@bp.route('/_load_versions', methods=['GET'])
def load_versions():
    model_id = request.args.get('model_id', 0, type=int)
    try:
        versions = Version.query.filter(Version.model_id == model_id).all()
        return jsonify(success=True, data=[v.serializable for v in versions])
    except:
        return jsonify(success=False)

@bp.route('/_save_orders', methods=['POST'])
def save_orders():
    form = OrderForm()
    # add value to form for form validate
    form.car.choices = [(form.data.get('car'), '')]
    form.model.choices = [(form.data.get('model'), '')]
    form.version.choices = [(form.data.get('version'), '')]
    form.customer.data = form.data.get('customer')

    if request.method == 'POST' and form.validate():
        try:
            orders = Order(
                cars=Car.query.get(form.data.get('car')),
                models=Model.query.get(form.data.get('model')),
                versions=Version.query.get(form.data.get('version')),
                customer_name=form.data.get('customer')
            )
            db_session.add(orders)
            db_session.commit()
            return jsonify(success=True)
        except:
            return jsonify(success=False)
