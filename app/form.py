# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import SelectField, TextField, validators


class OrderForm(Form):
    cars = SelectField(u'Car', coerce=int)
    models = SelectField(u'Model', choices=[('', '--choose--')])
    versions = SelectField(u'Version', choices=[('', '--choose--')])
    customer_name = TextField(u'Customer', [validators.InputRequired('Customer is required.')])
    