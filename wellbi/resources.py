from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import pgeocode
import geopy.distance
import heapq

bp = Blueprint('resources', __name__, url_prefix='/resources')

clinic_list = [['Castro-Mission Health Center', {'lat': 37.7631636584137, 'lng': -122.43202042310821}],
                    ['Lyon-Martin Women’s Health Services', {'lat': 37.769627008041525, 'lng': -122.4198499752374}],
                    ['Tom Waddell Health Center', {'lat': 37.779073814363635, 'lng': -122.41836942751574}],
                    ['Haight-Ashbury Free Medical Clinic', {'lat': 37.771016131782325, 'lng': -122.44843816450916}],
                    ['Mission Neighborhood Health Center', {'lat': 37.765220269982855, 'lng': -122.41662428341466}],
                    ['Southeast Health Center', {'lat': 37.7261632575225, 'lng': -122.39228857523872}],
                    ['Chinatown Public Health Center', {'lat': 37.79745393449752, 'lng': -122.41150583106013}],
                    ['North East Medical Services', {'lat': 37.800108351119306, 'lng': -122.40896287893071}],
                    ['Cole Street Youth Clinic', {'lat': 37.770099563710545, 'lng': -122.45043984455516}],
                    ['Sister Mary Philippa Health Center', {'lat': 37.773146543209776, 'lng': -122.45307070776671}],
                    ['Childrens Health Center at SFGH', {'lat': 37.756585087094145, 'lng': -122.40427153925992}],
                    ['Family Health Center at SFGH', {'lat': 37.75750031858322, 'lng': -122.40611502751149}],
                    ['Native American Health Center', {'lat': 37.76424155557056, 'lng': -122.41870581571993}],
                    ['Potrero Hill Health Center', {'lat': 37.754232430120844, 'lng': -122.39893124270846}],
                    ['Women’s Health Center at SFGH', {'lat': 37.754779729781255, 'lng': -122.40567247282607}],
                    ['San Francisco Free Clinic', {'lat': 37.78493320501721, 'lng': -122.47006635804873}],
                    ['Hip Hop to Health', {'lat': 37.714599013912654, 'lng': -122.46688415989787}],
                    ['South of Market Health Center', {'lat': 37.77967993403819, 'lng': -122.40940407523719}],
                    ['Ocean-Park Health Center', {'lat': 37.7624928425454, 'lng': -122.48262381571989}],
                    ['Larkin Street Youth Clinic', {'lat': 37.7882815769076, 'lng': -122.4192406733899}],
                    ['Curry Senior Center', {'lat': 37.782823847673576, 'lng': -122.4145124598959}],
                    ['St. Anthony Free Medical Clinic', {'lat': 37.78241964606527, 'lng': -122.41320307339001}],
                    ['Silver Avenue Family Health Center', {'lat': 37.732595039016246, 'lng': -122.40644320222667}],
                    ['Maxine Hall Health Center', {'lat': 37.779490497968744, 'lng': -122.42917569242543}]]


class getclinicsForm(FlaskForm):
    zipcode = StringField('Zipcode', validators=[DataRequired(), Length(5)])
    submit = SubmitField('Search')

def findClosest(form):
    zip = form.zipcode.data
    nomi = pgeocode.Nominatim('us')
    user_loc = nomi.query_postal_code(zip)
    user_coords = (user_loc['latitude'], user_loc['longitude'])
    closest = {}
    for i in range(len(clinic_list)): #carry out calculations to actually find closest clinics
        clinic_coords = (clinic_list[i][1]['lat'], clinic_list[i][1]['lng'])
        distance = geopy.distance.geodesic(user_coords, clinic_coords).miles
        closest[clinic_list[i][0]]= distance
    closest = heapq.nsmallest(5,closest,key=lambda x: (closest.get(x),x))
    return zip, closest


# Display diagnosis here
@bp.route('/clinics', methods=('GET', 'POST'))
def clinics():
    #print("here")
    form = getclinicsForm()
    if form.validate_on_submit():
        zipcode, closest = findClosest(form)
        return render_template("resources.html", form=form, zipcode=zipcode, clinics=closest)
    return render_template("resources.html", form=form)


@bp.route('/chlamydia', methods=('GET', 'POST'))
def chlamydia():
    form = getclinicsForm()
    if form.validate_on_submit():
        zipcode, closest = findClosest(form)
        return render_template("chlamydia_resources.html", form=form, zipcode=zipcode, clinics=closest)
    return render_template("chlamydia_resources.html", form=form)

@bp.route('/syphillis', methods=('GET', 'POST'))
def syphillis():
    form = getclinicsForm()
    if form.validate_on_submit():
        zipcode, closest = findClosest(form)
        return render_template("syphillis_resources.html", form=form, zipcode=zipcode, clinics=closest)
    return render_template("syphillis_resources.html", form=form)

@bp.route('/hepatitisC', methods=('GET', 'POST'))
def hepatitisC():
    form = getclinicsForm()
    if form.validate_on_submit():
        zipcode, closest = findClosest(form)
        return render_template("hepatitisC_resources.html", form=form, zipcode=zipcode, clinics=closest)
    return render_template("hepatitisC_resources.html", form=form)

@bp.route('/gonorrhea', methods=('GET', 'POST'))
def gonorrhea():
    form = getclinicsForm()
    if form.validate_on_submit():
        zipcode, closest = findClosest(form)
        return render_template("gonorrhea_resources.html", form=form, zipcode=zipcode, clinics=closest)
    return render_template("gonorrhea_resources.html", form=form)

@bp.route('/trichomoniasis', methods=('GET', 'POST'))
def trichomoniasis():
    form = getclinicsForm()
    if form.validate_on_submit():
        zipcode, closest = findClosest(form)
        return render_template("trichomoniasis_resources.html", form=form, zipcode=zipcode, clinics=closest)
    return render_template("trichomoniasis_resources.html", form=form)
