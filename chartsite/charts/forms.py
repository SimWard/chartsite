from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ChartForm(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired()])
    embed_text = TextAreaField('Content',
                               validators=[DataRequired()])
    submit = SubmitField('Submit')
