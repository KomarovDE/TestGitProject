import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
RESOURCE_SINGLE = 'api/unknown/2'
RESOURCE_NOT_FOUND = 'api/unknown/23'

#ДЗ
def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200

    users_data = response.json()['data']
    for item in users_data:
        validate(item, RESOURCE_DATA_SCHEMA)
        assert item['year'] >= 2000  # проверка year

def test_resource_single():
    response = httpx.get(BASE_URL + RESOURCE_SINGLE)
    assert response.status_code == 200

def test_resource_not_found():
    response = httpx.get(BASE_URL + RESOURCE_NOT_FOUND)
    assert response.status_code == 404