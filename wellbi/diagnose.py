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
    condition = request.args.get('diagnosis')
    if condition == 'Chlamydia':
        return redirect("/resources/chlamydia")
    elif condition == 'Gonorrhea':
        return redirect("/resources/gonorrhea")
    elif condition == 'Trichomoniasis':
        return redirect("/resources/trichomoniasis")
    elif condition == 'Syphillis':
        print('in diagnose.py if statement for syphillis')
        return redirect("/resources/syphillis")
    elif condition == 'Hepatitis C':
        return redirect("/resources/hepatitisC")
    else:
        return redirect("/resources/clinics")

# Display results here
@bp.route('/results', methods=('GET', 'POST'))
def results():
    curr_user_path = Path(__file__).parent.absolute()
    found_symptom = False
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


        for symptom in all_symptoms:
            checked = request.form.get(symptom)
            if checked:
                for index, row in df.iterrows():
                    symptoms = row["Symptoms"]
                    if symptom in symptoms:
                        disease_match[row["Disease"]] += 1 / len(row["Symptoms"].strip("[]").split(", "))
                        found_symptom = True


        sorted_disease_match = sorted(disease_match.items(), key = operator.itemgetter(1), reverse=True)
        other_possible_diseases = ""

        index = 0
        for each in sorted_disease_match:
            if each[1] > 0.05 and index > 0:
                other_possible_diseases += "<p> &ensp; " + each[0] + "</p>"
            index += 1

        curr_user_path=Path(__file__).parent.absolute()
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


            curr_user_path=Path(__file__).parent.absolute()
            diagnosis = sorted_disease_match[0][0]
            female_symptoms = df[(df["Disease"] == diagnosis) & (df["Gender"] == "Female")]["Symptoms"]
            common_f_symptoms = ""
            for each in female_symptoms:
                each = each.strip("[]").lower().split(", ")
                for i in range(len(each)):
                    if i == len(each) - 1:
                        common_f_symptoms += "and " + each[i]
                    else:
                        common_f_symptoms += each[i] + ", "

            male_symptoms = df[(df["Disease"] == diagnosis) & (df["Gender"] == "Male")]["Symptoms"]
            common_m_symptoms = ""
            for each in male_symptoms:
                each = each.strip("[]").lower().split(", ")
                for i in range(len(each)):
                    if i == len(each) - 1:
                        common_m_symptoms += "and " + each[i]
                    else:
                        common_m_symptoms += each[i] + ", "

            html += f"""
              <p> Please note: The results may not include your complete medical history and are provided solely for informational purposes and is not a substitute for professional medical advice. 
              </p>
              <div class = "results">
                <p><b> </b>From the symptoms you inputted it appears you may have {diagnosis}! 
                </p>
                <p> {diagnosis} is common in both men and women. 
                </p>
                <p>"""
            if common_f_symptoms != common_m_symptoms:
                html+=f"""
                    Common symptoms for females include {common_f_symptoms}.
                    </p>
                    <p>
                    Common symptoms for males include {common_m_symptoms}.
                    </p>"""
            else:
                html+=f"""
                    Common symptoms for {diagnosis} include {common_f_symptoms}.
                    </p>

            """
            html += f"""
                <div class = "recommendation">
                  <p> We recommend you make an appointment to see a medical professional.
                  </p>
                  <p><a href="{"{{"} url_for('diagnose.resources'){"}}"}">Find Resources on {diagnosis}</a>
                  
                  </p>
                </div>
              </div>
              </body>
            </div>"""


            if len(other_possible_diseases) != 0:
                html += f"""
                        <p>
                        Other disease(s) that match your symptoms may include: {other_possible_diseases}
                        </p>
                        <p><a href="{"{{"} url_for('diagnose.resources'){"}}"}">Find Additional Resources</a>

                        """
            html += f""" 

            <div class="Forums">
              <h4 class="header">Forums</h4>
              <p><a href="{"{{"} url_for('forum.search',tag='{diagnosis}'){"}}"}">Connect with Others about {diagnosis}</a>
              </p>
            </div>
            <div class="Feedback">
                  <h4 class="header">Feedback</h4>

            
                  <body>
                    <div class="rate" id="feedback">
                    <p> Was this information helpful?
                    </p>
                    <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" type="text/css" href="style.css">
                    <title>Star Rating</title>
                    </head>
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
                  <button id="button" onclick="submitRating()">Submit</button>
                  </div>
                  <script>
                            function submitRating() {"{"}
                                var feedback = document.getElementById("feedback");
                                feedback.innerHTML = "Thanks for submitting your feedback!"
                            {"}"}
                  </script>
                  </body>
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
