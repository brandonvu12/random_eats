from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    search = StringField('Search')
    submit = SubmitField('Submit')

class ResultForm(FlaskForm):
    name = StringField('Name')
    address = StringField('Address')
    rating = StringField('Rating')
    image = StringField('Image')
