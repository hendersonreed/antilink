import requests
import json


def test_basic_submit():
    api_url = 'http://localhost:5000/api/v1/submit'
    json_payload = {"url": "http://example.com"}
    response = requests.put(api_url, json=json_payload)
    breakpoint()
    print(response.json())
