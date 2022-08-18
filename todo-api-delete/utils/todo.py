from database.todo_db import table

def to_do_exists(todo_id:int) -> bool:
    retrieve_todo = table.get_item(Key={'id': todo_id})
    retrieve_todo = retrieve_todo.get('Item', None)
    if retrieve_todo:
        return True
    return False