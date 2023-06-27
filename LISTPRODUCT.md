## List Product API

The List Product API allows you to retrieve a list of available products.

### Endpoint

```
GET /list-products
```

### Request

- HTTP Method: GET
- API Endpoint: `https://n8crqa66x4.execute-api.us-east-1.amazonaws.com/dev/list-products`

### Response

The API response will contain a list of products in the following format:

```json
    {
    "LastEvaluatedKey": {
        "id": "633192b485f761e0d94b2bfd"
    },
    "statusCode": 200,
    "length": 10,
    "items": [
        {
            "productName": "Irish Potatoes",
            
            "category": "627cc5f7046919d2a6f2167d",
            "createdAt": "1663787083980",
            "images": [
                {
                    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1663787065/1663787064948.jpg",
                    "public_id": "1663787064948"
                }
            ],
            "sellerId": "632ab45bca9584f349e7f0e1",
            "productId": "632b604b0da9bd1d419a07db",
            "posterInfo": {
                "role": "seller",
                "firstName": "Yakubu",
                "lastName": "Rimamnungra",
                "profilePicUrl": "N/A"
            }
        },
        {
            "productName": "Brown Rabbit",
            
            "category": "627cc5f7046919d2a6f2167d",
            "createdAt": "1663787083980",
            "images": [
                {
                    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1663787065/1663787064948.jpg",
                    "public_id": "1663787064948"
                }
            ],
            "sellerId": "632ab45bca9584f349e7f0e1",
            "productId": "632b604b0da9bd1d419a07db",
            "posterInfo": {
                "role": "seller",
                "firstName": "Ajayi",
                "lastName": "Rafel",
                "profilePicUrl": [
                {
                    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1663787065/1663787064948.jpg",
                    "public_id": "1663787064948"
                }
            ],
            }
        }
        
    ]
}
```