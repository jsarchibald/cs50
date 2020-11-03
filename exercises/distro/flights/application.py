from flask import Flask, redirect, render_template, request
from cs50 import SQL
import time

from data import AIRPORTS
from helpers import insert_flight, to_timestamp


# Initialize the Flask app.
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.jinja_env.filters["to_timestamp"] = to_timestamp


# Open the database.
db = SQL("sqlite:///flights.db")


# Routes
@app.route("/")
def index():
    """Shows all the future flights in a table."""

    # Get flights
    flights = db.execute("SELECT * FROM flights WHERE departure >= ? ORDER BY departure;", time.time())

    # TODO: return the index.html template, passing in AIRPORTS and flights
    return "TODO"


@app.route("/add", methods=["GET", "POST"])
def add_flight():
    """Allows users to add flights."""

    if request.method == "GET":
        return render_template("add.html", airports=AIRPORTS)
    else:
        # Move request.form into a dictionary that's a bit shorter to access than request.form
        form = dict(request.form)

        # Change hour and minute into integers
        form["hour"] = int(form["hour"])
        form["minute"] = int(form["minute"])

        # TODO: Return error message if hour not in valid 0-23 range
        

        # TODO: Return error message if minute not in valid 0-59 range
        

        # TODO: Return error message if either airport not in AIRPORTS, or if they're equal


        # Insert into database
        insert_flight(db, form)

        # TODO: Redirect user to homepage
        return "TODO"


@app.route("/update/<flight_id>", methods=["GET", "POST"])
def update_flight(flight_id):
    """Updates a flight's status."""

    if request.method == "GET":
        # Get flight info
        flights = db.execute("SELECT * FROM flights WHERE id=?;", int(flight_id))
        if len(flights) < 1:
            return "No such flight!"

        flight = flights[0]

        # TODO: Return update.html template, passing in AIRPORTS and flight
        return "TODO"
    else:
        # TODO: If the status is not None, update the flight in the database
        

        # TODO: Redirect user to homepage
        return "TODO"
