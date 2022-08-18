import json
import boto3
from database.todo_db import table
from schemas.todo_schemas import TodoUpdateSchema
from pydantic import ValidationError
from json.decoder import JSONDecodeError
from botocore.exceptions import ClientError
from utils.todo import to_do_exists


def lambda_handler(event, context):
    try:
        todo_id = event["pathParameters"].get('todo-id', None)
        
        if not event.get('body', None):
            return {
                'statusCode': 400,
                'body': json.dumps({
                    "error": f"The body request MUST not be None"
                })
            }
            
        if not to_do_exists(todo_id):
            return {
                'statusCode': 404,
                'body': json.dumps({
                    "error": f"The To-do object with the id {todo_id} does not exist."
                })
            }
            
        todo_schema = TodoUpdateSchema(**json.loads(event.get('body', None)))
        response = table.update_item(
            Key={"id": todo_id},
            UpdateExpression="SET title = :title, description = :description ",
            ExpressionAttributeValues={
                ':title': todo_schema.title, 
                ':description': todo_schema.description
            },
            ReturnValues="UPDATED_NEW"
        )
        return {
            'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
            'body': json.dumps({
                "id": todo_id,
                "title": todo_schema.title,
                "description": todo_schema.description
            })
        }
            
    except (JSONDecodeError, ValidationError, ClientError) as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                "error": f"There was an error while updating the To-Do object. ---> {e}"
            })
        }

    

