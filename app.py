from datetime import datetime
from flask import Flask, jsonify, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

import os


PYTHON_DEADLINE = datetime(2022, 10, 14)
HTML_DEADLINE = datetime(2020, 10, 28)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

db.create_all()


# Models
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    feeling = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    script = db.Column(db.String(10000), nullable=False)
    workspace = db.Column(db.String(255), nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class HTMLSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    html = db.Column(db.String(100000), nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ip = db.Column(db.String(255))
    workspace = db.Column(db.String(255), nullable=False)


# Error handling
def error(message):
    response = jsonify({"message": str(message)})
    response.status_code = 400
    return response


# Routes (Python week)
@app.route("/")
def index():
    submissions = Submission.query.order_by(Submission.id.desc()).all()
    n = 6
    submissions = [submissions[i:i + n] for i in range(0, len(submissions), n)]  

    return render_template("index.html", submissions=submissions)


@app.route("/code/<int:sid>")
def code(sid):
    try:
        submission = Submission.query.filter_by(id=sid).first()
        return render_template("code.html", submission=submission)
    except:
        return error("Couldn't open the code for that submission.")


@app.route("/submission/<int:sid>", methods=["DELETE"])
def delete(sid):
    try:
        submission = Submission.query.filter_by(id=sid).first()
        db.session.delete(submission)
        db.session.commit()

        return "deleted, good job :)"
    except:
        return error("Something went wrong :(")


@app.route("/submission", methods=["POST"])
def submit():
    if datetime.now() > PYTHON_DEADLINE:
        return error("Past expiration date for Python submissions")

    fields = ["name", "year", "feeling", "url", "script", "_CS50_WORKSPACE_ID"]
    for field in fields:
        if request.form[field] is None:
            return error("Must provide data for all fields: {}".format(", ".join(fields)))
    
    try:
        submission = Submission(name=request.form["name"], 
                                year=int(request.form["year"]),
                                feeling=request.form["feeling"],
                                url=request.form["url"],
                                script=request.form["script"],
                                workspace = request.form["_CS50_WORKSPACE_ID"])
        db.session.add(submission)
        db.session.commit()

        return "good job :)"
    except:
        return error("Something went wrong :(")


# Routes (HTML/CSS/JS week)
@app.route("/html")
def html_index():
    submissions = HTMLSubmission.query.order_by(HTMLSubmission.id.desc()).all()

    return render_template("html.html", submissions=submissions)


@app.route("/html/<sid>")
def html_code(sid):
    try:
        submission = HTMLSubmission.query.filter_by(id=int(sid)).first()
        return submission.html
    except:
        return error("Couldn't open that submission.")


@app.route("/html/delete", methods=["POST"])
def html_delete():
    if request.form["id"] is None:
        return error("Must provide an ID to delete a submission")

    try:
        submission = HTMLSubmission.query.filter_by(id=int(request.form["id"])).first()
        db.session.delete(submission)
        db.session.commit()

        return "deleted, good job :)"
    except:
        return error("Something went wrong :(")


@app.route("/html/submit", methods=["POST"])
def html_submit():
    if datetime.now() > HTML_DEADLINE:
        return error("Past expiration date for HTML submissions")

    fields = ["title", "html"]
    for field in fields:
        if request.form[field] is None:
            return error("Must provide data for all fields: {}".format(", ".join(fields)))
    
    try:
        submission = HTMLSubmission(title=request.form["title"],
                                    html=request.form["html"],
                                    ip=request.remote_addr)
        db.session.add(submission)
        db.session.commit()

        return "good job :)"
    except:
        return error("Something went wrong :(")
