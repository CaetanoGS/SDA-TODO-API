from schemas.todo_schemas import TodoResponse

def resolve_todo_response(todo_obj):
    if type(todo_obj) == list:
        todo_items = []
        for todo_item in todo_obj:
            todo_items.append(TodoResponse(**todo_item).dict())
        return todo_items
    return TodoResponse(**todo_obj).dict()