# Create User API

The **Create User** API allows you to create a new user in the system.

## API Endpoint

```
POST https://n8crqa66x4.execute-api.us-east-1.amazonaws.com/dev/create-user
```

## Request Payload

The API expects the following JSON payload in the request body:

```json
{
  "activateUser": false,
  "currency": "NGN",
  "lastName": "Lamidi",
  "email": "example@email.com",
  "firstName": "John",
  "phone": "1234567890",
  "role": ["buyer", "seller"],
  "userName": "john123"
}
```


## Response

If the user is created successfully, the API will respond with a JSON payload containing the user details and a status code of 201 Created. The response body will look like this:

```json
{
  "userId": "h3fons893dfjg944ff",
  "activateUser": false,
  "createdAt": "1667213189880",
  "currency": "NGN",
  "lastName": "Lamidi",
  "email": "example@email.com",
  "firstName": "John",
  "phone": "1234567890",
  "role": ["buyer", "seller"],
  "id": "h3fons893dfjg944ff"
}
```

## Error Responses

If there is an error during the user creation process, the API will respond with an appropriate error status code and an error message in the response body.

- If the username already exists, the API will return a status code of 409 Conflict with the following response body:
  ```json
  {
    "error": "Username already exists"
  }
  ```

## Usage

To create a new user, send a POST request to the `/create-user` endpoint with the appropriate JSON payload in the request body.

## Conclusion

The **Create User** API provides a straightforward way to create new users in the system. Make sure to include all the required fields in the request payload for successful user creation.
