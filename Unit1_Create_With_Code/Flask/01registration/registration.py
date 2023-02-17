from flask_wtf import Form

from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators, ValidationError
from wtforms.validators import InputRequired, Email, EqualTo
from testemail import IsUnique

class Registration(Form):
    email = StringField("email", [validators.InputRequired ("please enter"), validators.Email('invalid email'), IsUnique])
    password = StringField("password", [validators.InputRequired("please enter")])
    confirm_password = StringField("confirm password", [validators.InputRequired("please enter"), validators.EqualTo("password", "passwords must match")])


    submit = SubmitField("Submit")
