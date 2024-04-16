from flask import Flask, request, jsonify
from readability import Document
from txtai.embeddings import Embeddings
import requests
from nanoid import generate


app = Flask(__name__)
embeddings = Embeddings(path="sentence-transformers/nli-mpnet-base-v2", content=True, objects=True)


@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"


@app.route('/api/v1/submit', methods=['PUT'])
def submit_url():
    data = request.get_json()
    if 'url' not in data:
        return jsonify({"error": "Invalid JSON data, please include a URL."}), 400
    url = data['url']
    data = requests.get(url)
    entry_object = {"text": Document(data.content).summary(), "url": url}
    entry_id = generate()

    embeddings.upsert([(entry_id, entry_object)])
    return jsonify({"id": entry_id})


@app.route('/api/v1/query_string', methods=['PUT'])
def query_string():
    """
    Accepts a string, returns N top results.
    The request data needs to look like
        {'query': 'the string to search for in the index', 'limit': N} where N is the maximum number of allowed results.
    """
    data = request.get_json()
    if 'query' not in data or 'limit' not in data:
        return jsonify({"error": "Invalid JSON data, please include a query and a limit."}), 400

    results = embeddings.search(data['query'], data['limit'])
    return jsonify(results)


@app.route('/api/v1/query_id', methods=['GET'])
def query_url():
    """
    Accepts an id of a URL that's in the DB, returns N top results.
    """
    raise NotImplementedError("This endpoint is not implemented")


def dev():
    app.run(debug=True)
