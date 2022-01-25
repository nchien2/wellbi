from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('resources', __name__, url_prefix='/resources')


# Display diagnosis here
@bp.route('/', methods=('GET', 'POST'))
def clinics():
    return render_template("resources.html")
