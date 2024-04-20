import datetime
import httpx
import pytest
import json
from jsonschema import validate
from core.contracts import SUCCESSFUL_REGISTERED_USER_SCHEMA, ERROR_RESPONSE_SCHEMA
import allure


BASE_URL = 'https://reqres.in'
REGISTER_ENDPOINT = '/api/register'
MISSED_EMAIL_ERROR = 'Missing email or username'
MISSED_PASSWORD_ERROR = 'Missing password'
json_file = open('D:/TestPythonProject/pythonProject/core/data_providers/registration_data.json')
registration_data = json.load(json_file)


@pytest.mark.parametrize('body', registration_data)
def test_register_user(body):
    response = httpx.post(BASE_URL + REGISTER_ENDPOINT, json=body)
    response_json = response.json()
    email = body['email']
    password = body['password']

    if len(email) > 0 and len(password) > 0:
        assert response.status_code == 200
        validate(response_json, SUCCESSFUL_REGISTERED_USER_SCHEMA)
    elif len(email) > 0:
        validate(response_json, ERROR_RESPONSE_SCHEMA)
        assert response.status_code == 400
        assert response_json['error'] == MISSED_PASSWORD_ERROR
    else:
        validate(response_json, ERROR_RESPONSE_SCHEMA)
        assert response.status_code == 400
        assert response_json['error'] == MISSED_EMAIL_ERROR