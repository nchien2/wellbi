import functools
from pathlib import Path
import operator
import pandas as pd

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
    return render_template("resources.html")

# Display results here
@bp.route('/results', methods=('GET', 'POST'))
def results():
    curr_user_path = Path(__file__).parent.absolute()

    if request.method == 'POST':
        df = pd.read_csv(str(curr_user_path) + "/static/Disease_Symptoms.csv")
        all_symptoms = set()
        for index, row in df.iterrows():
            symptoms = row["Symptoms"]
            symptoms = symptoms.strip("[]")
            symptoms = symptoms.split(", ")

            for sym in symptoms:
                all_symptoms.add(sym)

        disease_match = {}
        for index, row, in df.iterrows():
            disease_match[row["Disease"]] = 0

        found_symptom = False
        for symptom in all_symptoms:
            checked = request.form.get(symptom)
            if checked:
                found_symptom = True
                for index, row in df.iterrows():
                    symptoms = row["Symptoms"]
                    if symptom in symptoms:
                        disease_match[row["Disease"]] += 1
                        found_symptom = True

    html = """
    {% extends 'base.html' %}

    {% block header %}
      <h1 class = "header">{% block title %}Diagnose Me{% endblock %}</h1>
    {% endblock %}

    {% block content %}
    """
    if found_symptom == False:
        html += """
        <p> You didn't check any symptoms! Please restart the diagnosis process.  </p>
        """
    else:


        sorted_disease_match = sorted(disease_match.items(), key = operator.itemgetter(1), reverse=True)


        curr_user_path=Path(__file__).parent.absolute()
        diagnosis = sorted_disease_match[0][0]
        common_symptoms = ""

        html += f"""
          <p> Please note: The results may not include your complete medical history and are provided solely for informational purposes and is not a substitute for professional medical advice. 
          </p>
          <div class = "results">
            <p><b> </b>From the symptoms you inputted it appears you may have {diagnosis}! 
            </p>
            <p> {diagnosis} is common in both men and women.
            </p>
            <div class = "recommendation">
              <p> We recommend you make an appointment to see a medical professional.
              </p>
              <p><a href="{"{{"} url_for('diagnose.resources'){"}}"}">Find Resources on {diagnosis}</a>
              </p>
            </div>
            <div class="Feedback">
              <h3 class="header">Feedback</h3>
              <p> Was this information helpful?
              </p>
              <head>
              <meta charset="UTF-8">
              <link rel="stylesheet" type="text/css" href="style.css">
              <title>Star Rating</title>
              </head>
        
              <body>
              <div class="rate">
                <input type="radio" id="star5" name="rate" value="5" />
                <label for="star5" title="text">5 stars</label>
                <input type="radio" id="star4" name="rate" value="4" />
                <label for="star4" title="text">4 stars</label>
                <input type="radio" id="star3" name="rate" value="3" />
                <label for="star3" title="text">3 stars</label>
                <input type="radio" id="star2" name="rate" value="2" />
                <label for="star2" title="text">2 stars</label>
                <input type="radio" id="star1" name="rate" value="1" />
                <label for="star1" title="text">1 star</label>
              </div>
              </body>
            </div>
            <div class="Forums">
              <h4 class="header">Forums</h4>
              <p><a href="{"{{"} url_for('diagnose.forums'){"}}"}">Connect with Others</a>
              </p>
            </div>
          </div>
        """
    html += """
    {% endblock %}
    """
    file = open(str(curr_user_path) + "/templates/results.html", "w")
    file.write(html)
    file.close()
    return render_template("results.html")

# Display diagnosis here
@bp.route('/input', methods=('GET', 'POST'))
def input():
    return render_template("diagnose.html")