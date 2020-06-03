from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "6969669420694206969420"

from app import routes
