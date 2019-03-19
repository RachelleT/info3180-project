from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female','Female')])
    
    email = StringField('Email', validators=[InputRequired(), Email()])
    location = StringField('Location', validators=[InputRequired()])
    
    biography = TextAreaField('Biography', validators=[InputRequired()])
    
    photo = FileField('Profile Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])])
    
