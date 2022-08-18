import json
from database.todo_db import table
from botocore.exceptions import ClientError
from utils.todo import to_do_exists


def lambda_handler(event, context):
    try:
        todo_id = event["pathParameters"].get('todo-id', None)

        if not to_do_exists(todo_id):
            return {
                'statusCode': 404,
                'body': json.dumps({
                    "error": f"The To-do object with the id {todo_id} does not exist."
                })
            }
            
        response = table.delete_item(Key={"id": todo_id})
        
        return {
            'statusCode': 200,
            'body': json.dumps({"message": "To-Do object deleted successfully."})
        }
            
    except ClientError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                "error": f"There was an error while deleting the To-Do object."
            })
        }

    

