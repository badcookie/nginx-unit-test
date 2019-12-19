import json
import requests


def test_availability(base_url):
    url = f"{base_url}admin/"
    response = requests.get(url)
    assert response.status_code == 200


def test_static(base_url):
    url = f"{base_url}static/admin/css/base.css"
    response = requests.get(url)
    assert response.status_code == 200


def test_db(base_url):
    api_url = "api/v1/"
    url = f"{base_url}{api_url}"

    response = requests.get(f"{url}categories/")
    response_data = json.loads(response.content.decode("utf-8"))
    assert len(response_data) == 0
    assert response.status_code == 200

    response = requests.get(f"{url}categories/146")
    assert response.status_code == 404
