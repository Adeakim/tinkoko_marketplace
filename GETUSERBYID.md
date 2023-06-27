## Get User by ID API

The Get User by ID API allows you to retrieve a user by their unique identifier (ID).

### Endpoint

```
GET /user/{id}
```

### Request

- HTTP Method: GET
- API Endpoint: `https://n8crqa66x4.execute-api.us-east-1.amazonaws.com/dev/user/{id}`

Replace `{id}` in the API endpoint with the actual ID of the user you want to retrieve.

### Response

The API response will contain the user information in the following format:

```json
    {
    "id" "h3fons893dfjg944ff",
    "activateUser": false,
    "createdAt": "1667213189880",
    "currency": "NGN",
    "lastName": "Lamidi ",
    "email": "lamiditemitope31@email.com" ,
    "firstName": "Temitope ",
    "phone": "7043330737",
    "role": "sellerId",
    "userId": "temi247",
    }
```

### Example

To retrieve a user by their ID, you can send a GET request to the `/user/{id}` endpoint using a tool like Postman. Replace `{id}` in the API endpoint with the actual ID of the user you want to retrieve.

Here's an example using cURL:

```bash
curl -X GET https://n8crqa66x4.execute-api.us-east-1.amazonaws.com/dev/user/12345
```

Response:
```json
 {
    "id" "h3fons893dfjg944ff",
    "activateUser": false,
    "createdAt": "1667213189880",
    "currency": "NGN",
    "lastName": "Lamidi ",
    "email": "lamiditemitope31@email.com" ,
    "firstName": "Temitope ",
    "phone": "7043330737",
    "role": "sellerId",
    "userId": "temi247",
    }
```