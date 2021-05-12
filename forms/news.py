from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired, URL


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    url = StringField("Ссылка на партию", validators=[URL(require_tld=False, message=None)])
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')
