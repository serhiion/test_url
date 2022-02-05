from flask import Flask, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('settings')
ma = Marshmallow(app)
db = SQLAlchemy(app)


@app.route("/")
def index() -> str:
    return "http://0.0.0.0:5001/links/"

