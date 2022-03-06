import os

from flask import Flask
from wellbi import diagnose, forum, resources, profile, db_endpoints
from flask import render_template
import flask_login
# import django_heroku

#import * as React from 'react'

#import `ChakraProvider` component
#import { ChakraProvider } from '@chakra-ui/react'

#function App({ Component }) {
  #// 2. Use at the root of your app
  #return (
    #<ChakraProvider>
      #<Component />
    #</ChakraProvider>
  #)
#}

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        TEMPLATES_AUTO_RELOAD=True,
        RECAPTCHA_PUBLIC_KEY='6LeygGweAAAAAIvvb2mTz29PyDsxnMFWUOO4r0M_',
        RECAPTCHA_PRIVATE_KEY='6LeygGweAAAAAB_IQ9Rq4qi2uc8G1oitxp3LrjEl'
    )
    app.secret_key = 'c18f32f9f616b837c1b0'

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/home')
    @app.route('/')
    def home():
        return render_template("home.html")

    # register blueprints
    app.register_blueprint(diagnose.bp)
    app.register_blueprint(forum.bp)
    app.register_blueprint(resources.bp)
    app.register_blueprint(profile.bp)


    login_manager = flask_login.LoginManager()
    login_manager.login_view = 'profile.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # 1. Fetch against the database a user by `id`
        # 2. Create a new object of `User` class and return it.
        u_ref = db_endpoints.get_user_by_id(id)
        return profile.User(u_ref.to_dict()['username'])
    return app


app = create_app(None)
