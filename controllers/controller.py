from flask import render_template, request
from app import app
from models.events import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template("index.html", title="Home", events = events)

@app.route("/events", methods=[ "POST"])
def add_event():
    print(request.form)
    event_name = request.form["name"]
    event_date = request.form["date"]
    event_number_guests = request.form["number_guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    if "recurring" in request.form:
        event_recurring = request.form["recurring"]
    else:
        event_recurring = False
    new_event = Event(event_date, event_name, event_number_guests, event_location, event_description, event_recurring)
    add_new_event(new_event)
    return render_template("index.html", title= "Home", events = events) 