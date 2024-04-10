import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA
import allure

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
RESOURCE_SINGLE = 'api/unknown/2'
RESOURCE_NOT_FOUND = 'api/unknown/23'
COLOR_START = '#'

@allure.suite('Получение различных данных ресурса')
@allure.title('Получение списка ресурса')
def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    with allure.step (f'Проверка доступности ресурса'):
        assert response.status_code == 200

    test_resource_single = response.json()['data']
    for item in test_resource_single:
        validate(item, RESOURCE_DATA_SCHEMA)
        with allure.step(f'Проверка года'):
            assert item['year'] >= 2000  # проверка year
        with allure.step(f'Проверка {id}'):
            assert item['id'] >= 1 # проверка id


def test_resource_single():
    response = httpx.get(BASE_URL + RESOURCE_SINGLE)
    assert response.status_code == 200

    test_resource_single = response.json()['data']
    validate(test_resource_single, RESOURCE_DATA_SCHEMA)
    with allure.step(f'Проверка цвета {COLOR_START}'):
        assert test_resource_single['color'].startswith(COLOR_START) # проверка цвета
    with allure.step(f'Проверка {id}'):
        assert test_resource_single['id'] == 2


def test_resource_not_found():
    response = httpx.get(BASE_URL + RESOURCE_NOT_FOUND)
    with allure.step(f'Проверяем доступ к ресурсу'):
        assert response.status_code == 404