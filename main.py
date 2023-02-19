from flask import Flask, request, render_template, url_for, redirect, send_from_directory, send_file
import json
import random
import string
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        captcha_response = request.form['g-recaptcha-response']
        data = {
            'secret': "api key",
            'response': captcha_response
        }
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data).json()
        if r['success'] == True:
            return render_template("contact.html")
        else:
            return render_template("contact1.html")

    return render_template("contact1.html")

@app.route("/clicker")
def clicker_game():
    return redirect("https://docs.google.com/uc?export=download&id=1hQSZt_qBWt8TIDzgLZlsPack0zmY42Tr")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)