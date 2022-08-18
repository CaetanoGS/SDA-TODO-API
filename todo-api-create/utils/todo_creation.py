import uuid
from typing import Dict
from schemas.todo_schemas import TodoCreateSchema


def resolve_creation_request_body(request_body: Dict[str, str]) -> TodoCreateSchema:
    request_body['id'] = str(uuid.uuid4())
    return TodoCreateSchema(**request_body)