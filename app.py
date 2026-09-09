import os
from flask import Flask, g, request, render_template, url_for

#config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "User page: " + name + " - " + str(id)


@app.route('/object/<int:obj_id>')
def object_page(obj_id):
    return render_template('object.html')


if __name__ == "__main__":
    app.run(debug = True)