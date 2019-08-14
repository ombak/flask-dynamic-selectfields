# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import SelectField, TextField, HiddenField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class OrderForm(Form):
    car = SelectField(u'Car', choices=[('', '--choose--')])
    model = SelectField(u'Model', choices=[('', '--choose--')])
    version = SelectField(u'Version', choices=[('', '--choose--')])
    customer_name = TextField(u'Customer', [validators.InputRequired('Customer is required.')])


class OrderEditForm(Form):
    id = HiddenField(u'id')
    car = SelectField(u'Car', choices=[('', '--choose--')])
    model = SelectField(u'Model', choices=[('', '--choose--')])
    version = SelectField(u'Version', choices=[('', '--choose--')])
    customer_name = TextField(u'Customer', [validators.InputRequired('Customer is required.')])
