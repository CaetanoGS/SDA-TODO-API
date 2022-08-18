import json
from database.todo_db import table
from botocore.exceptions import ClientError
from schemas.todo_schemas import TodoResponse



def lambda_handler(event, context):
    try:
        todo_id = event["pathParameters"].get('todo-id', None)
        if not todo_id:
            return {
                'statusCode': 404,
                'body': json.dumps({
                    "error": f"There was an error loading the To-Do object with the following id {todo_id}."
                })
            }
        todo_obj = table.get_item(Key={'id': todo_id})
        todo_obj = todo_obj.get('Item', None)

        if not todo_obj:
            return {
                'statusCode': 404,
                'body': json.dumps({
                    "error": f"There was an error loading the To-Do object with the following id {todo_id}."
                })
            }
        return {
                'statusCode': 200,
                'body': json.dumps(TodoResponse(**todo_obj).dict())
            }
    except ClientError as e:
        return {
            'statusCode': 404,
            'body': json.dumps({
                "error": "There was an error loading the To-Do objects."
            })
        }


