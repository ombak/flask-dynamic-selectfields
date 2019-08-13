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

@bp.route('/edit_orders/<int:obj_id>/edit', methods=['GET'])
def edit_orders(obj_id):
    orders = Order.query.get(obj_id)
    form = OrderForm(obj=orders)
    form.cars.choices = [(c.id, c.car) for c in Car.query.order_by('id')]
    form.models.choices = [(m.id, m.model) for m in Model.query.filter(Model.car_id == orders.cars.id).all()]
    form.versions.choices = [(v.id, v.version) for v in Version.query.filter(Version.model_id == orders.models.id).all()]
    
    return render_template('edit_order.html', title="Edit Orders", form=form)


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
    form.cars.choices = [(form.data.get('cars'), '')]
    form.models.choices = [(form.data.get('models'), '')]
    form.versions.choices = [(form.data.get('versions'), '')]
    form.customer_name.data = form.data.get('customer_name')

    if request.method == 'POST' and form.validate():
        try:
            orders = Order(
                cars=Car.query.get(form.data.get('cars')),
                models=Model.query.get(form.data.get('models')),
                versions=Version.query.get(form.data.get('versions')),
                customer_name=form.data.get('customer_name')
            )
            db_session.add(orders)
            db_session.commit()
            return jsonify(success=True)
        except:
            return jsonify(success=False)

@bp.route('/_populate_table', methods=['GET'])
def populate_table():
    orders = Order.query.all()
    return jsonify(data=[o.serializable for o in orders])