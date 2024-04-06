import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
RESOURCE_SINGLE = 'api/unknown/2'
RESOURCE_NOT_FOUND = 'api/unknown/23'
COLOR_START = '#'

def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200

    test_resource_single = response.json()['data']
    for item in test_resource_single:
        validate(item, RESOURCE_DATA_SCHEMA)
        assert item['year'] >= 2000  # проверка year
        assert item['id'] >= 1 # проверка id

def test_resource_single():
    response = httpx.get(BASE_URL + RESOURCE_SINGLE)
    assert response.status_code == 200

    test_resource_single = response.json()['data']
    validate(test_resource_single, RESOURCE_DATA_SCHEMA)
    assert test_resource_single['color'].startswith(COLOR_START) # проверка цвета
    assert test_resource_single['id'] <= 7
def test_resource_not_found():
    response = httpx.get(BASE_URL + RESOURCE_NOT_FOUND)
    assert response.status_code == 404