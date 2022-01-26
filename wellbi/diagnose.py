import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('diagnose', __name__, url_prefix='/diagnose')

# Display forum here
@bp.route('/forums', methods=('GET', 'POST'))
def forums():
    return redirect("/forum/community")

# Display resources here
@bp.route('/resources', methods=('GET', 'POST'))
def resources():
    return render_template("chlamydia_resources.html")

# Display results here
@bp.route('/results', methods=('GET', 'POST'))
def results():
    return render_template("results.html")

# Display diagnosis here
@bp.route('/input', methods=('GET', 'POST'))
def input():
    return render_template("diagnose.html")