import boto3
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = 'userTable'
table = dynamodb.Table(table_name)

def get_user_by_username(event, context):
    path_params = event['pathParameters']
    user_name = path_params['userName']

    try:
        response = table.query(
            KeyConditionExpression=Key('userName').eq(user_name)
        )
        
        items = response.get('Items')
        
        if items:
            return {
                'statusCode': 200,
                'body': json.dumps({"data": items})
            }
        else:
            return {
                'statusCode': 404,
                'body': 'Item not found'
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
