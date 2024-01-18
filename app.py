from flask import Flask, jsonify
import os

app = Flask(__name__)


week_day = os.getenv("WEEK_DAY", "DEFAULT_WEEK")
weather_month = os.getenv("WEATHER_MONTH", "DEFAULT_MONTH")
weather = os.getenv("WEATHER", "DEFAULT_WEATHER")

@app.route("/")
def hello_world():
    return "<p>Ouuuuu yeahhhhh!!!</p>"

@app.route("/configmap")
def read_configmap():
    return "<p>Es {} hoy, normalmente en {} el tiempo es {}</p>".format(week_day, weather_month, weather)

@app.route("/flask-healthz")
def return_healthy():
    return "Estoy bien, gracias por preguntar", 200
