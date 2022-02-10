from pathlib import Path
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import flask_login
from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

from wellbi import db_endpoints

bp = Blueprint('forum', __name__, url_prefix='/forum')
curr_user_path = Path(__file__).parent.absolute()

class newPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Post')

class commentForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Post Comment')

@bp.route('result', methods=['POST'])
def result():
    title = request.form["new thread title"]
    description = request.form["new thread description"]
    with open(str(curr_user_path) + "/templates/thread.txt", "a") as f:
        f.write("\n" + title + ", " + description)
    refresh_thread()
    return redirect("/forum/community")


def refresh_thread():
    HTML_String = """
    {% extends 'base.html' %}

    {% block header %}
      <h1>{% block title %}Wellbi Forum{% endblock %}</h1>
    {% endblock %}

    {% block content %}
    <h3>
    New Thread
    </h3>
    <div class="threads">
    <form action = "result" method = "POST">
    <label for="new thread title">Title:</label>
    <br>
    <input type="text" style="width:400px;" id = "new thread title" name="new thread title">
    <br>
    <label for="new thread description">Details:</label>
    <br>
    <input type="text" style="height:100px;width:400px;" id = "new thread description" name="new thread description">
    <br>
    <br>
    <input type = "submit">
    </form>
    </div>
    <br>
    <h3>
    Browse Existing Threads
    </h3>
    <div class="threads">
    """
    with open(str(curr_user_path) + "/templates/thread.txt") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.split(",")
        HTML_String += f"""
        <li class="row">
                <h4 class="title">
                    {parts[0]}
                </h4>
                <div class="bottom">
                    <p>
                        {parts[1]} 
                    </p>
                </div>
        </li>"""

    HTML_String += """
    </div>
    <style>
            p {
                margin: 5px 0;
            }
            .row {
                padding: 5px 0;
            }
            .bottom {
                display: flex;
                color: grey;
                font-size: 12px;
                margin: 5px 5px;
            }
            .threads {
                margin: 10px 60px;
            }
    </style>
    {% endblock %}
    """
    file = open(str(curr_user_path) + "/templates/forum.html", "w")
    file.write(HTML_String)
    file.close()


# Display diagnosis here
@bp.route('/community')
def community():
    return render_template("forum.html")

@bp.route('/show_post')
def show_post():
    form = commentForm()
    post_id = request.args.get('post_id')
    post_dict = db_endpoints.get_post_by_id(post_id)
    value_dict = {
        'title': post_dict['title'], 
        'body': post_dict['body'], 
        'username': post_dict['author']
    }
    # post_dict = session['post']
    # session.pop('post')
    # print(type(post_dict))
    # print(post_dict)
    return render_template("post.html", form=form, post_dict=value_dict)

@bp.route('/new_post', methods=('GET', 'POST'))
@login_required
def new_post():
    form = newPostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        username = flask_login.current_user.username
        # user_ref = db_endpoints.get_user_by_id(username)
        # - post = db_endpoints.make_post(title, body, username).get().to_dict()
        # - session['post'] = {'title': title, 'body': body, 'username': username}
        post_id = db_endpoints.make_post(title, body, username).get().id
        
        # print(post['post_title'])
        return redirect(url_for("forum.show_post", post_id=post_id))
    return render_template("make_post.html", form=form)

