#!/usr/bin/env python

import json
import subprocess
from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

# Process should be a que to enable multiple subprocesses
process = None


@app.route("/")
def index():
    """Returns information about the command and possible routes"""
    with open('config.json') as configfile:
        configdata = json.load(configfile)

    return jsonify({'name': configdata['title'],
                    'version': configdata['version'],
                    'description': configdata['description'],
                    'routes': [
                        {
                            'path': '/run',
                            'method': ['POST'],
                            'description': 'Send POST to execute command'
                        },
                        {
                            'path': '/result',
                            'method': ['GET'],
                            'description': 'Get results, if result: false it still runs'
                        },
                        {
                            'path': '/config',
                            'method': ['GET'],
                            'description': 'Get available commands'
                        }]
                    })


@app.route("/run", methods=['POST','HEAD'])
def run():
    """Starts the subproccess"""
    global process

    req = request.get_json(force=True)

    execute = req.get('command')

    process = subprocess.Popen(execute, shell=True, stdout=subprocess.PIPE)
    return jsonify({"message": "Subprocess started"})


@app.route("/result")
def result():
    """Read the result from the subprocess """
    global process

    if not process:
        return jsonify({"status": 1, "response": "No running proccess"})
    elif not process.poll() == 0:
        return jsonify({"status": 2, "response": "Process still running"})

    res = process.communicate()
    process.kill()
    process = None
    return jsonify({"status": 0, "response": str(res[0])})


@app.route("/config", methods=['GET'])
def config():
    """Used is container is external"""
    with open('config.json') as configfile:
        return jsonify(json.load(configfile))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
