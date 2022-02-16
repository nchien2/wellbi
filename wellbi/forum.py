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
# import db_endpoints

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
    return redirect("/forum/community")

# Show top posts
@bp.route('/community')
def community():
    title_list, id_list = db_endpoints.get_top_posts()
    return render_template('forum.html', title_list=title_list, id_list=id_list)

@bp.route('/show_post', methods=['POST'])
@login_required
def comment_show_post():
    form = commentForm()

    if form.validate_on_submit():
        post_id = request.args.get('post_id')
        body = form.body.data
        username = flask_login.current_user.username
        # user_ref = db_endpoints.get_user_by_id(username)
        # - post = db_endpoints.make_post(title, body, username).get().to_dict()
        # - session['post'] = {'title': title, 'body': body, 'username': username}        
        
        # print(post['post_title'])
        db_endpoints.make_comment(content=body, username=username, post_id=post_id)
    return redirect(url_for("forum.show_post", post_id=post_id))

@bp.route('/show_post', methods=(['GET']))
def show_post():
    form = commentForm()
    post_id = request.args.get('post_id')
    post_dict = db_endpoints.get_post_by_id(post_id)
    value_dict = {
        'title': post_dict['title'], 
        'body': post_dict['body'], 
        'username': post_dict['author']
    }
    content_list, author_list = db_endpoints.get_comments(post_id)
    return render_template("post.html", form=form, post_dict=value_dict, post_id=post_id, \
                           contents=content_list, authors=author_list)

@bp.route('/new_post', methods=('GET', 'POST'))
@login_required
def new_post():
    form = newPostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        username = flask_login.current_user.username
        post_id = db_endpoints.make_post(title, body, username).get().id
        
        return redirect(url_for("forum.show_post", post_id=post_id))
    return render_template("make_post.html", form=form)

