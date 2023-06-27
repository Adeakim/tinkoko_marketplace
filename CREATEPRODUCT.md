# Create Product API

The **Create Product** API allows you to create a new product in the system.

## API Endpoint

```
POST https://n8crqa66x4.execute-api.us-east-1.amazonaws.com/dev/create-product
```

## Request Payload

The API expects the following JSON payload in the request body:

```json
{
  "category": "627cc555046919d2a6f21662",
  "city": "Abuja",
  "count": 10,
  "country": "Nigeria",
  "description": "Banana Flavour Minimum Order Quantity - 10pcs",
  "images": [
    {
      "public_id": "n4t5ccur0shvzrnwlkoy",
      "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
    }
  ],
  "price": "1000",
  "productName": "L&Z Yoghurt",
  "quantity": 100,
  "subCategory": "hLBxpm6XoCWvhQQdsmRjQPZL",
  "sellerId": "634084c8fd2c16ba75c006e8",
  "weight": "500"
}
```

## Response

If the product is created successfully, the API will respond with a JSON payload containing the product details and a status code of 200 OK. The response body will look like this:

```json
{
  "id": "h3fons893dfjg944ff",
  "category": "627cc555046919d2a6f21662",
  "city": "Abuja",
  "count": 10,
  "country": "Nigeria",
  "createdAt": "1667213189880",
  "description": "Banana Flavour Minimum Order Quantity - 10pcs",
  "images": [
    {
      "public_id": "n4t5ccur0shvzrnwlkoy",
      "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
    }
  ],
  "price": "1000",
  "productName": "L&Z Yoghurt",
  "quantity": 100,
  "subCategory": "hLBxpm6XoCWvhQQdsmRjQPZL",
  "sellerId": "634084c8fd2c16ba75c006e8",
  "weight": "500"
}
```

If there is an error during the creation process, the API will respond with an appropriate error message and a corresponding status code.

## Usage

To create a new product, send a POST request to the API endpoint mentioned above with the required payload in the request body. You can use any HTTP client to make the request, such as cURL or Postman.

Here's an example using cURL:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "category": "627cc555046919d2a6f21662",
  "city": "Abuja",
  "count": 10,
  "country": "Nigeria",
  "description": "Banana Flavour Minimum Order Quantity - 10pcs",
  "images": [
    {
      "public_id": "n4t5ccur0shvzrnwlkoy",
      "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
    }
  ],
  "price": "1000",
  "productName": "L&Z Yoghurt",
  "quantity": 100,
  "subCategory": "hLBxpm6XoCWvhQQdsmRjQPZL",
  "sellerId": "634084c8fd2c16ba75c006e8",
  "weight": "500"
}' https://n8crqa66x4.execute-api.us-east-1.amazonaws.com/dev/create-product
```
