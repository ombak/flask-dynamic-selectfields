# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import SelectField


class DropdownForm(Form):
    car = SelectField(u'Car', coerce=int)
    model = SelectField(u'Model', coerce=int)
    version = SelectField(u'Version', choices=[('', '--choose--')])
