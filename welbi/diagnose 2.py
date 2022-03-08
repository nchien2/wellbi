import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('diagnose', __name__, url_prefix='/diagnose')


# Display diagnosis here
@bp.route('/results', methods=('GET', 'POST'))
def results():
    return render_template("results.html")

# Display diagnosis here
@bp.route('/input', methods=('GET', 'POST'))
def input():
    return render_template("diagnose.html")