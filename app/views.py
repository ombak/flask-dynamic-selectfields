# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify, request, url_for
from .forms import OrderForm, OrderEditForm
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
    form = OrderEditForm()
    form.car.choices = [(c.id, c.car) for c in Car.query.all()]
    form.model.choices = [(m.id, m.model) for m in Model.query.filter(Model.car_id == orders.cars.id).all()]
    form.version.choices = [(v.id, v.version) for v in Version.query.filter(Version.model_id == orders.models.id).all()]
    
    form.id.default = orders.id
    form.car.default = orders.cars.id
    form.model.default = orders.models.id
    form.version.default = orders.versions.id
    form.customer_name.default = orders.customer_name
    form.process()

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
    car_id = request.args.get('id', 0, type=int)
    try:
        models = Model.query.filter(Model.car_id == car_id).all()
        return jsonify(success=True, data=[m.serializable for m in models])
    except:
        return jsonify(success=False)

@bp.route('/_load_versions', methods=['GET'])
def load_versions():
    model_id = request.args.get('id', 0, type=int)
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
    form.customer_name.data = form.data.get('customer_name')

    if request.method == 'POST' and form.validate():
        try:
            order = Order(
                cars=Car.query.get(form.data.get('car')),
                models=Model.query.get(form.data.get('model')),
                versions=Version.query.get(form.data.get('version')),
                customer_name=form.data.get('customer_name'))
            db_session.add(order)
            db_session.commit()
            
            return jsonify(
                        success=True, 
                        messages=[u'Submited successfully'],
                        next=url_for('main.index'))
        except:
            return jsonify(success=False, errors=True, messages=form.errors)

@bp.route('/_update_orders', methods=['POST'])
def update_orders():
    form = OrderEditForm()
    form.car.choices = [(form.data.get('car'), '')]
    form.model.choices = [(form.data.get('model'), '')]
    form.version.choices = [(form.data.get('version'), '')]
    form.customer_name.data = form.data.get('customer_name')
    
    if request.method == 'POST' and form.validate():
        try:
            id = form.data.get('id')
            order = Order.query.get(id)
            order.cars=Car.query.get(form.data.get('car'))
            order.models=Model.query.get(form.data.get('model'))
            order.versions=Version.query.get(form.data.get('version'))
            order.customer_name=form.data.get('customer_name')
        
            db_session.add(order)
            db_session.commit()
            return jsonify(
                        success=True,
                        messages=[u'Updated successfully'],
                        next=url_for('main.index'))
        except:
            return jsonify(success=False, errors=True, messages=form.errors)

@bp.route('/_populate_table', methods=['GET'])
def populate_table():
    orders = Order.query.all()
    return jsonify(data=[o.serializable for o in orders])
