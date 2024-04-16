from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"


@app.route('/api/v1/submit', methods=['PUT'])
def submit_url():
    data = request.get_json()
    if 'url' in data:
        url = data['url']
        data = requests.get(url)
        breakpoint()
        return jsonify({"message": "URL submitted successfully", "html": "test"})
    else:
        return jsonify({"error": "Invalid JSON data"}), 400


def dev():
    app.run(debug=True)
