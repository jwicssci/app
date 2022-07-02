from dataclasses import dataclass
import psutil
import subprocess
from app import app
from flask import render_template, request, json, jsonify, redirect


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


@app.route("/getjson", methods=["GET", "POST"])
# url -X POST http://localhost:5000/json -H "Content-Type: application/json" -d @data.json
def handle_json():
    if (request.method == 'POST') and request.is_json:
        req = request.get_json()
        return "JSON received", 200
    elif (request.method == 'GET'):
        # output = subprocess.run(['cat', '/tmp/nvidia.json'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        cmd = "nvidia-smi -x -q |xml2json| jq"
        ps = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = json.loads(ps.communicate()[0])
        gpu = (result['nvidia_smi_log']['gpu']['product_name'])
        gpu_memory_usage = (result['nvidia_smi_log']
                            ['gpu']['fb_memory_usage']['used'])
        gpu_memory_free = (result['nvidia_smi_log']
                           ['gpu']['fb_memory_usage']['free'])
        gpu_current_temp = (result['nvidia_smi_log']
                            ['gpu']['temperature']['gpu_temp'])
        gpu_power_usage = (result['nvidia_smi_log']
                           ['gpu']['power_readings']['power_draw'])
        gpu_clock_speed = (result['nvidia_smi_log']
                           ['gpu']['clocks']['graphics_clock'])
        cpu_temp = psutil.sensors_temperatures()['k10temp'][1]
        cpu_current_temp = str(cpu_temp.current)

        return render_template("public/getjson.html", gpu=gpu, gpu_memory_usage=gpu_memory_usage, gpu_memory_free=gpu_memory_free, gpu_current_temp=gpu_current_temp, gpu_power_usage=gpu_power_usage, gpu_clock_speed=gpu_clock_speed, cpu_current_temp=cpu_current_temp)
    else:
        return "Invalid request!", 400
