USER_DATA_SCHEMA = {
    "type": "object",  # бывает еще array - массив, если число - number, если текст - string.
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"},
    },
    "required": ["id", "email", "first_name", "last_name", "avatar"]
}

RESOURCE_DATA_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "year": {"type": "number"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"},
    },
    "required": ["id", "name", "year", "color", "pantone_value"]
}

CREATED_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "required": ["name", "job", "id", "createdAt"]
}

UPDATED_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"},
    },
    "required": ["name", "job", "updatedAt"]
}

SUCCESSFUL_REGISTERED_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "token": {"type": "string"},
    },
    "required": ["id", "token"]
}

SUCCESSFUL_LOGIN_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "token": {"type": "string"},
    },
    "required": ["token"]
}

ERROR_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "error": {"type": "string"},
    },
    "required": ["error"]
}

