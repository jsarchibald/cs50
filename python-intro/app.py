from datetime import datetime
from flask import Flask, jsonify, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///submissions.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Models
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    feeling = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    script = db.Column(db.String(10000), nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


# Error handling
def error(message):
    response = jsonify({"message": str(message)})
    response.status_code = 400
    return response


# Routes
@app.route("/")
def index():
    submissions = Submission.query.order_by(Submission.id.desc()).all()
    n = 6
    submissions = [submissions[i:i + n] for i in range(0, len(submissions), n)]  

    return render_template("index.html", submissions=submissions)


@app.route("/code/<sid>")
def code(sid):
    try:
        submission = Submission.query.filter_by(id=int(sid)).first()
        return render_template("code.html", submission=submission)
    except:
        return error("Couldn't open the code for that submission.")


@app.route("/delete", methods=["POST"])
def delete():
    if request.form["id"] is None:
        return error("Must provide an ID to delete a submission")

    try:
        submission = Submission.query.filter_by(id=int(request.form["id"])).first()
        db.session.delete(submission)
        db.session.commit()

        return "deleted, good job :)"
    except:
        return error("Something went wrong :(")


@app.route("/submit", methods=["POST"])
def submit():
    fields = ["name", "year", "feeling", "url", "script"]
    for field in fields:
        if request.form[field] is None:
            return error("Must provide data for all fields: {}".format(", ".join(fields)))
    
    try:
        submission = Submission(name=request.form["name"], 
                                year=int(request.form["year"]),
                                feeling=request.form["feeling"],
                                url=request.form["url"],
                                script=request.form["script"])
        db.session.add(submission)
        db.session.commit()

        return "good job :)"
    except:
        return error("Something went wrong :(")

