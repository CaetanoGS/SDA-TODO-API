import json
from database.todo_db import table
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    try:
        todo_id = event["pathParameters"].get('todo-id', None)
        if not todo_id:
            return {
                'statusCode': 404,
                'body': json.dumps({
                    "error": "Not Found"
                })
            }
        todo_obj = table.get_item(Key={'id': todo_id})
        todo_obj = todo_obj.get('Item', None)

        if not todo_obj:
            return {
                'statusCode': 404,
                'body': json.dumps({
                    "error": "Not Found."
                })
            }
        return {
                'statusCode': 200,
                'body': json.dumps(todo_obj)
            }
    except ClientError as e:
        return {
            'statusCode': 404,
            'body': json.dumps({
                "error": f"There was an error loading the To-Do objects. ---> {e}"
            })
        }


