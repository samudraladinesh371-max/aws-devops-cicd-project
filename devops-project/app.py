From flask import flask

name=Flask(__name__)
@app.route("/"):
    return "Devops CI/CD PROJECT SUCCESSFULLY RUNNING"
app.run(hos="0.0.0.0/0" port=5000)
