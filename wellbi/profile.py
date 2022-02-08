import functools
from . import db_endpoints
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('profile', __name__, url_prefix='/profile')

class loginForm(FlaskForm):
    uname = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Log in')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('test')
        username = form.uname.data
        password = form.password.data
        user_dict = db_endpoints.get_user(username, password)
        return redirect(url_for('profile.display', username=username))
    return render_template('login.html', form=form, username='temp')


@bp.route('/', methods=('GET', 'POST'))
def display():
    username = request.args['username']
    return render_template('profile.html', username=username)
# # Display forum here
# @bp.route('/user', methods=('GET', 'POST'))
# def user():
#     if request.method=='POST':
        
    
#     return render_template('profile.html')