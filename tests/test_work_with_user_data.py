import datetime
import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEMA
from core.contracts import PUT_UPDATED_USER_SCHEMA
from core.contracts import PATCH_UPDATED_USER_SCHEMA
import allure

BASE_URL = 'https://reqres.in/api/users'
BASE_URL_U = 'https://reqres.in/api/users/2'


@allure.suite('Rest методы')
@allure.title('Create{name, job}')
def test_create_user_with_name_and_job():
    body = {                                           # BODY ЗАПРОСА
        "name": "dmitry",
        "job": "leader"
    }                                                  # BODY ЗАПРОСА
    print(body['name'])

    response = httpx.post(BASE_URL, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    creation_date = response_json['createdAt'].replace('T', ' ')
    with allure.step(f'Проверка доступности ресурса'):
        assert response.status_code == 201

    validate(response_json, CREATED_USER_SCHEMA)
    with allure.step(f'Проверка имени response_json["name"]'):
        assert response_json['name'] == body['name'], 'Имя в ответе совпадает с ожидаемым'
    with allure.step(f'Проверка должности response_json["job"]'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверка времени'):
        assert creation_date[0:16] == current_date[0:16]

    print(creation_date)
    print(current_date)


@allure.suite('Rest методы')
@allure.title('Create{name}')
def test_create_user_with_name():
    body = {                                           # BODY ЗАПРОСА
        "name": "Dmitry"
    }                                                  # BODY ЗАПРОСА
    print(body['name'])

    response = httpx.post(BASE_URL, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    creation_date = response_json['createdAt'].replace('T', ' ')
    with allure.step(f'Проверка доступности ресурса'):
        assert response.status_code == 201
    validate(response_json, CREATED_USER_SCHEMA)


@allure.suite('Rest методы')
@allure.title('Create{job}')
def test_create_user_with_job():
    body = {                                           # BODY ЗАПРОСА
        "job": "leader"
    }                                                  # BODY ЗАПРОСА
    print(body['name'])

    response = httpx.post(BASE_URL, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    creation_date = response_json['createdAt'].replace('T', ' ')
    with allure.step(f'Проверка доступности ресурса'):
        assert response.status_code == 201
    validate(response_json, CREATED_USER_SCHEMA)


@allure.suite('Rest методы')
@allure.title('Create{}')
def test_create_user_with_empty_body():
    body = {                                           # BODY ЗАПРОСА
        "name": "",
        "job": ""
    }                                                  # BODY ЗАПРОСА

    response = httpx.post(BASE_URL, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    creation_date = response_json['createdAt'].replace('T', ' ')
    with allure.step(f'Проверка доступности ресурса'):
        assert response.status_code == 201
    validate(response_json, CREATED_USER_SCHEMA)
    with allure.step(f'Проверка имени response_json["name"]'):
        assert response_json['name'] == body['name'], 'Имя в ответе совпадает с ожидаемым'
    with allure.step(f'Проверка должности response_json["job"]'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверка времени'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Rest методы')
@allure.title('put_update{name, job}')
def test_update_user_with_name_and_job():
    body = {  # BODY ЗАПРОСА
        "name": "Nedmitry",
        "job": "worker"
    }  # BODY ЗАПРОСА

    print(body['name'])
    print(body['job'])

    response = httpx.put(BASE_URL_U, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    creation_date = response_json['updatedAt'].replace('T', ' ')
    with allure.step(f'Проверка доступности ресурса'):
        assert response.status_code == 200
    validate(response_json, PUT_UPDATED_USER_SCHEMA)
    with allure.step(f'Проверка имени response_json["name"]'):
        assert response_json['name'] != "Dmitry", 'Имя в ответе не совпадает с ожидаемым'
    with allure.step(f'Проверка должности response_json["job"]'):
        assert response_json['job'] != "leader"
    with allure.step(f'Проверка времени'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Rest методы')
@allure.title('patch_update{name, job}')
def test_update_user_with_name_and_job():
    body = {  # BODY ЗАПРОСА
        "name": "Samson",
        "job": "boss"
    }  # BODY ЗАПРОСА

    print(body['name'])
    print(body['job'])

    response = httpx.patch(BASE_URL_U, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    creation_date = response_json['updatedAt'].replace('T', ' ')
    with allure.step(f'Проверка доступности ресурса'):
        assert response.status_code == 200
    validate(response_json, PATCH_UPDATED_USER_SCHEMA)
    with allure.step(f'Проверка имени response_json["name"]'):
        assert response_json['name'] != "Nedmitry", 'Имя в ответе не совпадает с ожидаемым'
    with allure.step(f'Проверка должности response_json["job"]'):
        assert response_json['job'] != "worker"
    with allure.step(f'Проверка времени'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Rest методы')
@allure.title('Delete{name, job}')
def test_delete_user_with_name_and_job():

    response = httpx.delete(BASE_URL_U)
    with allure.step(f'Проверка доступности ресурса'):
        assert response.status_code == 204
