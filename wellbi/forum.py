from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('forum', __name__, url_prefix='/forum')

@bp.route('result', methods=['POST'])
def result():
    title = request.form["new thread title"]
    description = request.form["new thread description"]
    with open("/Users/tiffanyshi/Desktop/seniorproject/Team21/wellbi/templates/thread.txt", "a") as f:
        f.write("\n" + title + ", " + description)
    refresh_thread()
    return redirect("/forum/community")


def refresh_thread():
    HTML_String = """
    {% extends 'base.html' %}

    {% block header %}
      <h1>{% block title %}Wellbi Forum{% endblock %}</h1>
    {% endblock %}

    {% block content %}
    <h3>
    New Thread
    </h3>
    <div class="threads">
    <form action = "result" method = "POST">
    <label for="new thread title">Title:</label>
    <br>
    <input type="text" style="width:400px;" id = "new thread title" name="new thread title">
    <br>
    <label for="new thread description">Details:</label>
    <br>
    <input type="text" style="height:100px;width:400px;" id = "new thread description" name="new thread description">
    <br>
    <br>
    <input type = "submit">
    </form>
    <button onClick="window.location.reload();">Post</button>
    </div>
    <br>
    <h3>
    Browse Existing Threads
    </h3>
    <div class="threads">
    """
    with open("/Users/tiffanyshi/Desktop/seniorproject/Team21/wellbi/templates/thread.txt") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.split(",")
        HTML_String += f"""
        <li class="row">
                <h4 class="title">
                    {parts[0]}
                </h4>
                <div class="bottom">
                    <p>
                        {parts[1]} 
                    </p>
                </div>
        </li>"""

    HTML_String += """
    </div>
    <style>
            p {
                margin: 5px 0;
            }
            .row {
                padding: 5px 0;
            }
            .bottom {
                display: flex;
                color: grey;
                font-size: 12px;
                margin: 5px 5px;
            }
            .threads {
                margin: 10px 60px;
            }
    </style>
    {% endblock %}
    """
    file = open("/Users/tiffanyshi/Desktop/seniorproject/Team21/wellbi/templates/forum.html", "w")
    file.write(HTML_String)
    file.close()


# Display diagnosis here
@bp.route('/community')
def community():
    return render_template("forum.html")
