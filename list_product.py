import boto3
from boto3.dynamodb.conditions import Attr
import json

def list_products(event, context):
    dynamodb = boto3.resource('dynamodb')
    product_table = dynamodb.Table('Product')
    user_table = dynamodb.Table('userTable')

    response = product_table.scan(Limit=5)
    products = response.get('Items', [])

    seller_ids = [product['sellerId'] for product in products]
    sellers_map = {}

    for seller_id in seller_ids:
        seller_response = user_table.scan(FilterExpression=Attr('id').eq(seller_id))
        sellers = seller_response.get('Items')
        if sellers:
            seller = sellers[0]
            sellers_map[seller_id] = {
                'role': seller.get('role', ''),
                'firstName': seller.get('firstName', ''),
                'lastName': seller.get('lastName', ''),
                'profilePicUrl': seller.get('profilePic', '')
            }

    response_payload = {
        'LastEvaluatedKey': response.get('LastEvaluatedKey', {}),
        'statusCode': 200,
        'length': len(products),
        'items': []
    }

    for product in products:
        seller_id = product['sellerId']
        seller = sellers_map.get(seller_id, {})
        product_info = {
            'productName': product['productName'],
            'category': product['category'],
            'createdAt': product['createdAt'],
            'images': product['images'],
            'sellerId': seller_id,
            'productId': product['id'],
            'posterInfo': {
                'role': seller.get('role', ''),
                'firstName': seller.get('firstName', ''),
                'lastName': seller.get('lastName', ''),
                'profilePicUrl': seller.get('profilePicUrl', '')
            }
        }
        response_payload['items'].append(product_info)

    return  {
        'statusCode': 200,
        'body': json.dumps(response_payload)
    }

