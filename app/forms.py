from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EncodeForm(FlaskForm):
    data = StringField("Data", validators = [DataRequired()])
    submit = SubmitField("Encode")

class DecodeForm(FlaskForm):
    data = StringField("Data", validators = [DataRequired()])
    submit = SubmitField("Decode")
