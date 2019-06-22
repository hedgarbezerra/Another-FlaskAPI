# API REST usando framework Flask com SQLAlchemy e Marshmallow
 
## How-To

# Endpoint de usuários

### Listar todos usuários

**Definição/Request**

`GET /v1/users`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": [
        {
            "created_on": "2019-06-20T01:49:12+00:00",
            "email": "uew2141w@gmail.c1om",
            "id": 7,
            "name": "Hector",
            "password": "pbkdf2:sha256:150000$JTZXWfaO$9f81b13091bf87bdc7883f55089efec6421e3ed076d3bbc3bb4476b6b4b8d39f",
            "username": "hector4413"
        },
        {
            "created_on": "2019-06-20T02:09:35+00:00",
            "email": "uewasdasd41w@gmail.c1om",
            "id": 9,
            "name": "Hedgar",
            "password": "pbkdf2:sha256:150000$JTZXWfaO$9f81b13091bf87bdc7883f55089efec6421e3ed076d3bbc3bb4476b6b4b8d39f",
            "username": "hedgsahj"
        },
        {
            "created_on": "2019-06-20T14:49:06+00:00",
            "email": "uewasd41w@gmail.c1om",
            "id": 10,
            "name": "Hedgar",
            "password": "pbkdf2:sha256:150000$JTZXWfaO$9f81b13091bf87bdc7883f55089efec6421e3ed076d3bbc3bb4476b6b4b8d39f",
            "username": "hed"
        }
    ],
    "message": "successfully fetched"
}
```
### Listar usuários filtrando por nome

**Definição/Request**

`GET /v1/users?name=a`

**Response**

- `200 OK` ao ter sucesso

```json
{
    "data": [
        {
            "created_on": "2019-06-20T02:09:35+00:00",
            "email": "uewasdasd41w@gmail.c1om",
            "id": 9,
            "name": "Hedgar",
            "password": "pbkdf2:sha256:150000$JTZXWfaO$9f81b13091bf87bdc7883f55089efec6421e3ed076d3bbc3bb4476b6b4b8d39f",
            "username": "hedgsahj"
        },
        {
            "created_on": "2019-06-20T14:49:06+00:00",
            "email": "uewasd41w@gmail.c1om",
            "id": 10,
            "name": "Hedgar",
            "password": "pbkdf2:sha256:150000$JTZXWfaO$9f81b13091bf87bdc7883f55089efec6421e3ed076d3bbc3bb4476b6b4b8d39f",
            "username": "hed"
        }
    ],
    "message": "successfully fetched"
}
```


## Retornar um usuário especifico

`GET /v1/users/<id>`

**Response**

- `404 Not Found` usuário não existe

```json
{
    "data": {},
    "message": "user don't exist"
}
```

- `200 OK` ao ter sucesso

```json
{
    "data": {
        "created_on": "2019-06-20T02:09:35+00:00",
        "email": "uewasdasd41w@gmail.c1om",
        "id": 9,
        "name": "Hedgar",
        "password": "hecto1r1234",
        "username": "hedgsahj"
    },
    "message": "successfully fetched"
}
```


### Registrando novo usuário

**Definição/Request**

`POST /v1/users`

**Argumentos**

- `"username":string` usuário que será mostrado e feito para usar a api
- `"password":string` senha que será encriptada antes de ir para o banco
- `"name":string` nome do usuário
- `"email":string` email que será usado para comunicação

**Response**

- `201 Created` ao ter sucesso

```json
{
    "data": {
        "created_on": "2019-06-20T19:38:35+00:00",
        "email": "uewasdx41w@gmail.c1om",
        "id": 11,
        "name": "Hedgar",
        "password": "pbkdf2:sha256:150000$1GZZJmHH$671c1dffb868b6dc72b459fb3c2cb8cd2dd547b4d4f64834139469a562dc4b0a",
        "username": "hexd"
    },
    "message": "successfully registered"
}
```

- `200 Created` ao ter erro com usuário ou email existente

```json
{
    "data": {
        },
    "message": "user already exists"
}
```

- `500 Internal error` ao ter erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "unable to create"
}
```


### Atualizando usuário

**Definição/Request**

`PUT /v1/users/<id>`

**Argumentos**

- `"username":string` usuário que será mostrado e feito para usar a api(eventualmente)
- `"password":string` senha que será encriptada antes de ir para o banco(eventualmente)
- `"name":string` nome do usuário
- `"email":string` email que será usado para comunicação(caso necessário)

**Response**

- `201 Created` ao ter sucesso

```json
{
    "data": {
        "created_on": "2019-06-20T02:09:35+00:00",
        "email": "uewaxsd41w@gmail.c1om",
        "id": 9,
        "name": "Hedgar",
        "password": "pbkdf2:sha256:150000$zm6vMaTn$eedf14ff2b30a449e52be4a96ae0533d437faba3869ae93d7297e5036f2f4ffc",
        "username": "hex1x11d"
    },
    "message": "successfully updated"
}
```

- `404 Not Found` usuário não existe

```json
{
    "data": {},
    "message": "user don't exist"
}
```

- `500 Internal error` ao ter erro com servidor ou sistema

```json
{
    "data": {},
    "message": "unable to update"
}
```

## Deletar usuário

**Definição**

`DELETE /v1/users/<id>`

**Response**

- `200 No Content` ao ter sucesso

```json
{
    "data": {
        "created_on": "2019-06-20T01:38:55+00:00",
        "email": "uewuhe11w@gmail.com",
        "id": 3,
        "name": "Hector",
        "password": "hector1234",
        "username": "hector12113"
    },
    "message": "successfully deleted"
}
```

- `404 Not Found` usuário não existente

```json
{
    "data": {},
    "message": "user don't exist"
}
```

- `500 Internal error` erro com servidor ou sistema

```json
{
    "data": {},
    "message": "unable to delete"
}
```

## Autenticação do token com servidor JWT

`POST /v1/auth`

**No header do seu JavaScript será necessário passar os dados do usuário.**

***Authorization: 'Basic ' + btoa(username + ':' + password)***

**Response**

- `401 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
 "token": "QIHWEUkoqwe8291j1ioe2j12jjw9218.JASJA.WQIUH3uijs0a",
 "exp": "Mon, 20 May 2019 10:45:50 GMT"
}
```


