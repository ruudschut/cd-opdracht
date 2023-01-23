from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def client():
    return "<p>Home, sweet home.</p>"

@app.route("/greet/")
def grt():
    return "<h1>Hello, world!</h1>"

@app.route("/greet/<example_name>")
def grt_name(example_name):
    return f"<h1>Hello, {escape(example_name)}!</h1>"