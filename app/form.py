# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import SelectField, TextField, validators


class OrderForm(Form):
    car = SelectField(u'Car', choices=[('', '--choose--')])
    model = SelectField(u'Model', choices=[('', '--choose--')])
    version = SelectField(u'Version', choices=[('', '--choose--')])
    customer = TextField(u'Customer', [validators.InputRequired('Customer is required.')])
    