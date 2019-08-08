from flask import Blueprint, render_template
from .form import DropdownForm
from .db import get_db

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    db = get_db()
    form = DropdownForm()
    
    cars = db.execute('SELECT id, name FROM car').fetchall()
    form.car.choices = [(c['id'], c['name']) for c in cars]

    models = db.execute('SELECT id, model FROM model WHERE car_id = ?', (1, )).fetchall()
    form.model.choices = [(m['id'], m['model']) for m in models]    
    

    return render_template('form.html', form=form)
