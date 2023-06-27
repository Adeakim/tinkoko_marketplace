import boto3
import json
from uuid import uuid4
import time
from boto3.dynamodb.conditions import Key


def create_user(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('userTable')
    
    request_body = json.loads(event['body'])
    
    username = request_body['userName']
    response = table.query(
        KeyConditionExpression=Key('userName').eq(username))
    print(response)
    
    if len(response["Items"]) > 0:
        return {
            'statusCode': 409,
            'body': json.dumps({'error': 'Username already exists'})
        }
    
    user_id = str(uuid4())
    
    try:
        user = {
            'userId': user_id,
            'activateUser': request_body['activateUser'],
            'createdAt': str(int(time.time() * 1000)),
            'currency': request_body['currency'],
            'lastName': request_body['lastName'],
            'email': request_body['email'],
            'firstName': request_body['firstName'],
            'phone': request_body['phone'],
            'role': request_body['role'],
            'userName': username
        }
        table.put_item(Item=user)
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
    
    response_payload = {
        'userId': user_id,
        'activateUser': user['activateUser'],
        'createdAt': user['createdAt'],
        'currency': user['currency'],
        'lastName': user['lastName'],
        'email': user['email'],
        'firstName': user['firstName'],
        'phone': user['phone'],
        'role': user['role'],
        'id': user['userId']
    }
    
    response = {
        'statusCode': 201,
        'body': json.dumps(response_payload)
    }
    
    return response
