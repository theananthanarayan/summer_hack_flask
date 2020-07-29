from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user 
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField, ValidationError, TextField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from summer_hack_flask import db
from summer_hack_flask.models import User
import phonenumbers


class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Confirm Password must match Password')])

    phone = StringField('Phone', validators=[DataRequired()], render_kw={"placeholder": "+(country_code) (XXX) XXX-XXXX"})
    firstname = TextField('First Name:', validators=[DataRequired()])
    lastname = TextField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')

    #Validating username
    def validate_username(self, username):
        if User.objects(username = username.data):
            raise ValidationError('That username is taken. Please choose a different one.')

    #Validating email
    def validate_email(self, email):
        if User.objects(email=email.data):
            raise ValidationError('This email ID is already registered. Please use a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()], render_kw={"placeholder": "eg. Italian, Mexican, Indian or Name any specific cuisine"})

    explanation = TextAreaField('Description', validators=[DataRequired()], render_kw={"placeholder": "Describe your item in a few words"})

    radius = SelectField('Choose your comfortable distance (in mi):', coerce=int, choices=[(2,'2'),(5,'5'),(10,'10'),(15,'15'),(25,'25')], validators=[DataRequired()])

    postType = RadioField('Would you like to:', choices=[('give','Post an Offering'),('ask','Request for an Offering')], validators=[DataRequired()])

    submit = SubmitField('Submit')