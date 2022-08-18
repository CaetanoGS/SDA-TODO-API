import json
from utils.todo_creation import resolve_creation_request_body
from pydantic import ValidationError
from json.decoder import JSONDecodeError
from botocore.exceptions import ClientError
from database.todo_db import table

def lambda_handler(event, context):
    try:
        if not event.get('body', None):
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "Creation body request MUST not be None"})
            }
        
        request_body = resolve_creation_request_body(json.loads(event.get('body', None)))
        response = table.put_item(Item=request_body.dict())
        return {
            'statusCode': 201,
            'body': json.dumps(request_body.dict())
        }
    except (JSONDecodeError, ValidationError, ClientError) as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                "error": f"There was an error while creating the To-Do object. ---> {e}"
            })
        }
    
