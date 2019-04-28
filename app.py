from flask import Flask, render_template, request, redirect
import os
import logging
import random

app = Flask(__name__, template_folder=os.getcwd())

os.environ['NLS_LANG'] = 'RUSSIAN_CIS.CL8MSWIN1251'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('applogfile.txt')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route("/")
def home():
    return redirect("/index", code=302)

@app.route("/index", methods = ['GET'])
def action():
    return render_template("index.html", color="white")

@app.route("/index", methods = ['POST'])
def index():
    if "red" in request.form:
        logger.info('red')
        color = "red"
    elif "green" in request.form:
        logger.info('green')
        color = "green"
    elif "blue" in request.form:
        logger.info('blue')
        color = "blue"
    elif "yellow" in request.form:
        logger.info('yellow')
        color = "yellow"
    elif "reset" in request.form:
        logger.info('white')
        color = "white"
    return render_template("/index.html", color=color)

if __name__ == "__main__":
    app.run(debug=True)