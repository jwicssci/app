from dataclasses import dataclass
import os
from re import L
import subprocess
from app import app
from flask import render_template, request, json, jsonify, redirect


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template("public/about.html")

# url -X POST http://localhost:5000/json -H "Content-Type: application/json" -d @data.json


@app.route("/getjson", methods=["GET", "POST"])
def handle_json():
    if (request.method == 'POST') and request.is_json:
        req = request.get_json()
        return "JSON received", 200
    elif (request.method == 'GET'):
        nvidia = subprocess.run(['cat', '/tmp/nvidia.json'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        return (nvidia)
        # return render_template("public/getjson.html", nvidia=str)
    else:
        return "Invalid request!", 400
