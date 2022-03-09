from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('forum', __name__, url_prefix='/forum')


# Display diagnosis here
@bp.route('/community')
def community():
    return render_template("forum.html")
