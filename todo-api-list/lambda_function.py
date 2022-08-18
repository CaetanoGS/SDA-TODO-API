import json
from database.todo_db import table
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    response = table.scan()
    if not response.get('Items', None):
        return {
            'statusCode': 200,
            'body': json.dumps([])
        }
    return {
        'statusCode': 200,
        'body': json.dumps(response.get('Items', None))
    }
