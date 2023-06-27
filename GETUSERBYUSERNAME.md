## Get User by Username API

The Get User by Username API allows you to retrieve a user by their username.

### Endpoint

```
GET /get-user/{username}
```

### Request

- HTTP Method: GET
- API Endpoint: `https://n8crqa66x4.execute-api.us-east-1.amazonaws.com/dev/get-user/{username}`

Replace `{username}` in the API endpoint with the actual username of the user you want to retrieve.

### Response

The API response will contain the user information in the following format:

```json
{
      {
    "id":"h3fons893dfjg944ff",
    "activateUser": false,
    "createdAt": "1667213189880",
    "currency": "NGN",
    "lastName": "Lamidi ",
    "email": "lamiditemitope31@email.com" ,
    "firstName": "Temitope ",
    "phone": "7043330737",
    "role": "buyer",
    "userId": "temi247",
    }
}
```

### Example

To retrieve a user by their username, you can send a GET request to the `/get-user/{username}` endpoint using a tool like Postman. Replace `{username}` in the API endpoint with the actual username of the user you want to retrieve.

Here's an example using cURL:

```bash
curl -X GET https://n8crqa66x4.execute-api.us-east-1.amazonaws.com/dev/get-user/johndoe
```
