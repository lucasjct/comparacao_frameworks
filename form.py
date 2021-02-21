from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class LoginNostalgic(FlaskForm):

    nome = StringField('nome', validators=[DataRequired()])
    sobrenome = StringField('sobrenome', validators=[DataRequired()])
    email = StringField('email', validators=DataRequired)
    genero = SelectField('genero', validators=DataRequired)
    mensagem = SelectField('mensagem')