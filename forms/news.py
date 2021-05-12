from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, Form
from wtforms.validators import DataRequired, URL, InputRequired, ValidationError


class MyValid(object):
    def __init__(self):
        self.messege = 'Wrong URL, try another one'

    def __call__(self, form, field):
        url = field.data
        if url != '':
            if url[:8] != 'https://':
                raise ValidationError(self.messege)


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    url = StringField('Ссылка на партию', validators=[MyValid()])
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')
