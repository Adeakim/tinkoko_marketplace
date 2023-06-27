import boto3
import json
import time
from uuid import uuid4
from boto3.dynamodb.conditions import Attr

def create_product(event, context):
    dynamodb = boto3.resource('dynamodb')
    product_table = dynamodb.Table('Product')
    user_table = dynamodb.Table('userTable')

    try:
        request_body = json.loads(event['body'])

        seller_id = request_body['sellerId']
        response = user_table.scan(FilterExpression=Attr('userId').eq(seller_id))
        print(seller_id)
        print(response)

        if len(response['Items']) == 0:
            return {
                'statusCode': 409,
                'body': json.dumps({'error': 'SellerId does not exist'})
            }

        product_id = str(uuid4())
        product = {
            'id': product_id,
            'category': request_body['category'],
            'city': request_body['city'],
            'count': request_body['count'],
            'country': request_body['country'],
            'createdAt': str(int(time.time() * 1000)),
            'description': request_body['description'],
            'images': request_body['images'],
            'price': request_body['price'],
            'productName': request_body['productName'],
            'quantity': request_body['quantity'],
            'subCategory': request_body['subCategory'],
            'sellerId': request_body['sellerId'],
            'weight': request_body['weight']
        }
        product_table.put_item(Item=product)

        response_payload = {
            'id': product_id,
            'category': product['category'],
            'city': product['city'],
            'count': product['count'],
            'country': product['country'],
            'createdAt': product['createdAt'],
            'description': product['description'],
            'images': product['images'],
            'price': product['price'],
            'productName': product['productName'],
            'quantity': product['quantity'],
            'subCategory': product['subCategory'],
            'sellerId': product['sellerId'],
            'weight': product['weight']
        }

        response = {
            'statusCode': 200,
            'body': json.dumps(response_payload)
        }

        return response
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
