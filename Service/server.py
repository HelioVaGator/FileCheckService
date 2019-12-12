import os
from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/validateFile', methods=['POST'])
def validateFile():
    print("Posted file: {}".format(request.files['file']))
    blob = request.files['file'].read()
    print(str(len(blob)))

    return str(json_validator(blob))

@app.route("/")
def index():
    return render_template("index.html");


def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)