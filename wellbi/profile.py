import functools
import db_endpoints, __init__
from flask_wtf import FlaskForm, Recaptcha, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask import current_app as app
import flask_login
from flask_login import login_required

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('profile', __name__, url_prefix='/profile')


class User:
    def __init__(self, username):
        self.username = username
        self.active=True

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            user_id, user_dict = db_endpoints.get_user(self.username, 'temp')
            return user_id
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __eq__(self, other):
        '''
        Checks the equality of two `User` objects using `get_id`.
        '''
        if isinstance(other, User):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        '''
        Checks the inequality of two `User` objects using `get_id`.
        '''
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal


class loginForm(FlaskForm):
    uname = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class signupForm(FlaskForm):
    uname = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    recaptcha = RecaptchaField(validators=[Recaptcha(message="Recaptcha failed. Try again.")])
    submit = SubmitField('Sign up')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        username = form.uname.data
        password = form.password.data
        id, user_dict = db_endpoints.get_user(username, password)
        if not id:
            flash('Username ' + username + ' not found. Try again.')
            return redirect(url_for('profile.login', type='login'))
        if password != user_dict['password']:
            flash('Invalid password.')
            return render_template('login.html', form=form, type='login')
        logged_user = User(username)
        flask_login.login_user(logged_user, remember=True)
        print(flask_login.current_user.is_authenticated())
        return redirect(url_for('profile.display', username=flask_login.current_user.username))
    return render_template('login.html', form=form, type='login')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = signupForm()
    if form.validate_on_submit():
        username = form.uname.data
        password = form.password.data
        password2 = form.password2.data
        if password != password2:
            flash('Passwords do not match.')
            return redirect(url_for('profile.signup'))
        id, user_dict = db_endpoints.get_user(username, password, update=True)
        # If the user with username already exists, return to signup
        print(id)
        if id:
            flash('Email address already exists.')
            return redirect(url_for('profile.signup', type='signup'))

        logged_user = User(username)
        flask_login.login_user(logged_user, remember=True)
        return redirect(url_for('profile.display', username=username))
    return render_template('login.html', form=form, type='signup')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def display():
    username = flask_login.current_user.username
    user_obj = db_endpoints.get_user_by_id(username)
    posts = user_obj.to_dict()['posts']
    print(posts)

    title_list =[]
    id_list = []
    for post_ref in posts:
        post = post_ref.get()
        title_list.append(post.to_dict()['title'])
        id_list.append(post.id)
    print(id_list)
    print(title_list)
    return render_template('profile.html', username=username, title_list=title_list, id_list=id_list)

@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    flask_login.logout_user()
    return redirect(url_for('profile.login'))
