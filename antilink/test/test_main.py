import requests

base_url = "http://localhost:5000/api/v1"


def test_basic_workflow():
    """
    This ensures that the
        1. basic "submit" functionality is working,
        2. we can query

    wherein a url gets submitted and the response is a positive status
    code and a snip of json with an id.
    """

    # basic submit functionality
    api_url = f'{base_url}/submit'
    json_payload1 = {"url": "http://example.com"}
    json_payload2 = {"url": "https://python.org"}
    submit_response1 = requests.put(api_url, json=json_payload1)
    submit_response2 = requests.put(api_url, json=json_payload2)
    assert submit_response1.status_code == 200
    assert submit_response2.status_code == 200
    assert 'id' in submit_response1.json()
    assert 'id' in submit_response2.json()

    # does the retrieval work as expected?
    api_url = f'{base_url}/query_string'
    json_payload = {"query": "example", 'limit': 1}
    query_response = requests.put(api_url, json=json_payload)
    assert submit_response1.json()['id'] == query_response.json()[0]['id']

    api_url = f'{base_url}/query_string'
    json_payload = {"query": "Python", 'limit': 1}
    query_response = requests.put(api_url, json=json_payload)
    assert submit_response2.json()['id'] == query_response.json()[0]['id']
