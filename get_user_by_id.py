import boto3
import json
from boto3.dynamodb.conditions import Attr

def get_user_id(event, context):
    dynamodb = boto3.resource('dynamodb')
    user_table = dynamodb.Table('userTable')
    user_id = event['pathParameters']['userId']

    try:
        response = user_table.scan(
            FilterExpression=Attr('userId').eq(user_id)
        )

        items = response.get('Items')
        if items:
            user = items[0]
            return {
                'statusCode': 200,
                'body': json.dumps(user)
            }
        else:
            return {
                'statusCode': 404,
                'body': 'User not found'
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
