from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('resources', __name__, url_prefix='/resources')



# Display diagnosis here
@bp.route('/', methods=('GET', 'POST'))
def clinics():
    return render_template("resources.html")

@bp.route('/chlamydia', methods=('GET', 'POST'))
def chlamydia():
	return render_template("chlamydia_resources.html")

@bp.route('/syphillis', methods=('GET', 'POST'))
def syphillis():
	return render_template("syphillis_resources.html")

@bp.route('/herpes', methods=('GET', 'POST'))
def herpes():
	return render_template("herpes_resources.html")
