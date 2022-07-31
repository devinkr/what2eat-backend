# What2Eat Back End

## Description

A REST API built for [What2Eat](https://github.com/devinkr/where2eat).

## Technologies
  - Python
  - Django
  - Djano REST Framework
  - Simple JWT
  - PostgreSQL
  
## Endpoints

### Account Registration

`POST /api/register/`

#### Request
```json
{
  "username" : "username",
  "password" : "password",
  "password" : "password"
}
```


#### Response 201 Created
```json
{
    "username" : "username"
}
```

#### Response 400 Bad Request
```json
{
    "username": [
        "This field must be unique."
    ],
    "password": [
        "This password is too short. It must contain at least 8 characters.",
        "This password is too common."
    ]
}
```


### Account Login

`POST /api/token/`

#### Request
```json
{
  "username" : "username",
  "password" : "password"
}
```

#### Response 200 OK
```json
{
    "refresh": "JWT Refresh Token",
    "access": "JWT Access Token"
}
```

#### Response 401 Unauthorized
```json
{
    "detail": "No active account found with the given credentials"
}
```


### Token Refresh

`POST /api/token/refresh/`

#### Request
```json
{
  "refresh" : "JWT Refresh Token"
}
```

#### Response 200 OK
```json
{
    "access": "New JWT Access Token"
}
```

#### Response 401 Unauthorized
```json
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```


### Categories Index

`GET /api/categories/`
  - Authorization : Bearer Token
  - Will only return categories where authenticated user is the owner.

#### Response 200 OK
```json
[
    {
        "id": 6,
        "title": "Asian Cuisine",
        "owner": "username",
        "restaurants": [
            {
                "id": 5,
                "name": "Panda Express",
                "owner": "username",
                "categories": [
                    6,
                    7,
                    3
                ]
            },
            {
                "id": 13,
                "name": "Woo Ri",
                "owner": "username",
                "categories": [
                    6
                ]
            },
            {
                "id": 12,
                "name": "Yuan Palace",
                "owner": "username",
                "categories": [
                    6
                ]
            }
        ]
    }
]
```

#### Response 401 Unathorized
```json
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```


### Categories Create
`POST /api/categories/`
  - Authorization : Bearer Token

#### Request
```json
{
  "title" : "title of category"
}
```

#### Reponse 201 Created
```json
{
    "id": 10,
    "title": "title of category",
    "owner": "username",
    "restaurants": []
}
```

### Categories Delete
`DELETE /api/categories/id/`
  - Authorization : Bearer Token

#### Reponse 204 No Content


### Categories Detail
`GET /api/categories/id/`
  - Authorization : Bearer Token

#### Response 200 OK
```json
{
    "id": 2,
    "title": "Mexican",
    "owner": "username",
    "restaurants": [
        {
            "id": 10,
            "name": "Poblanos",
            "owner": "username",
            "categories": [
                7,
                3,
                2
            ]
        },
        {
            "id": 1,
            "name": "Taco Bell",
            "owner": "username",
            "categories": [
                3,
                2
            ]
        },
        {
            "id": 11,
            "name": "Torchy's",
            "owner": "username",
            "categories": [
                3,
                2
            ]
        }
    ]
}
```

#### Response 404 Not Found
When you try to access a category id that does not exist
```json
{
    "detail": "Not found."
}
```

#### Resonse 403 Forbidden
When you try to access a category id owned by a different user.
```json
{
    "detail": "You do not have permission to perform this action."
}
```

### Restuarants
`/api/restaurants/`
  - All the same CRUD endpoints exist for restaurants as for categories.


