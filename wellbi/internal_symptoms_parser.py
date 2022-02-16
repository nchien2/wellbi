import pandas as pd
from pathlib import Path
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('diagnose', __name__, url_prefix='/forum')
curr_user_path = Path(__file__).parent.absolute()


# Display results here
@bp.route('/results', methods=('GET', 'POST'))
def results():
    return render_template("results.html")


def create_checkboxes():
    HTML_String = """
    {% extends 'base.html' %}

    {% block header %}
        <h1>{% block title %}Diagnose Me{% endblock %}</h1>
    {% endblock %}
    
    <h2>Female</h2>
    
    {% block content %}
        <h3>Check the symptoms you are experiencing</h3>
        <form action={{ url_for('diagnose.results') }} method="post"> 
    """
    female_df = pd.read_csv(str(curr_user_path) + "/static/Disease_Symptoms.csv")
    female_df = female_df.loc[female_df["Gender"] == "Female"]
    all_symptoms = set()
    for index, row in female_df.iterrows():
        symptoms = row["Symptoms"]
        symptoms = symptoms.strip("[]")
        symptoms = symptoms.split(", ")

        for sym in symptoms:
            all_symptoms.add(sym)
    for each in all_symptoms:
        HTML_String += f"""
            <div>
                <input type="checkbox" id="{str(each)}" name="{str(each)}">
                <label for="{str(each)}">{str(each)}</label>
            </div>
        """

    HTML_String += """
    
    <h2>Male</h2>
    
    {% block content %}
        <h3>Check the symptoms you are experiencing</h3>
    """
    male_df = pd.read_csv(str(curr_user_path) + "/static/Disease_Symptoms.csv")
    male_df = male_df.loc[male_df["Gender"]=="Male"]
    all_symptoms = set()
    for index, row in male_df.iterrows():
        symptoms = row["Symptoms"]
        symptoms = symptoms.strip("[]")
        symptoms = symptoms.split(", ")

        for sym in symptoms:
            all_symptoms.add(sym)
    for each in all_symptoms:
        HTML_String += f"""
                <div>
                    <input type="checkbox" id="{str(each)}" name="{str(each)}">
                    <label for="{str(each)}">{str(each)}</label>
                </div>
            """

    HTML_String += """
    <input type="submit" value="Submit">
    </form>
    {% endblock %}
    """

    html_file = open(str(curr_user_path) + "/templates/diagnose.html", "w")
    html_file.write(HTML_String)
    html_file.close()


create_checkboxes()
