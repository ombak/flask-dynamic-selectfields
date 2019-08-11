from flask import Blueprint, render_template, jsonify, request
from .form import DropdownForm
from .models import Car, Model, Version


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = DropdownForm()
    car = form.car.choices = [(c.id, c.name) for c in Car.query.all()]
    model = form.model.choices = [(0, '--choose model--')]
    return render_template('form.html', form=form)