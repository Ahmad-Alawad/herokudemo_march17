import os

from flask import Flask, render_template, request
from flask import redirect, session as flask_session

# from model import db, Melon, connect_to_db


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")


@app.route("/")
def index():
    """Show homepage with number-of-visits count."""

    num = flask_session["visits"] = flask_session.get("visits", 0) + 1
    return render_template("index.html", num=num)


@app.route("/melons")
def melons():
    """Show list of melons from our database."""

    all_melons = db.session.query(Melon).all()
    return render_template("melons.html", melons=all_melons)


@app.route("/add-melon", methods=['POST'])
def add_melon():
    """Add a melon and redirect to list of melons."""

    name = request.form.get("name")
    melon = Melon(name=name)
    db.session.add(melon)
    db.session.commit()

    return redirect("/melons")


@app.route("/error")
def error():
    raise Exception("Error!")


if __name__ == '__main__':

    # First, suppose our application had no database.
    # Later, we'll uncomment this:
    # Connect our application to our database
    # connect_to_db(app, os.environ.get("DATABASE_URL"))
    # db.create_all()

    # PORT = int(os.environ.get("PORT", 5000))
    # DEBUG = "NO_DEBUG" not in os.environ

    app.run(host="0.0.0.0", debug=True)
    # app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
