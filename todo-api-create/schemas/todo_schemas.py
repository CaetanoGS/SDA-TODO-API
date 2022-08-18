from pydantic import BaseModel

class TodoCreateSchema(BaseModel):
    id: str
    title: str
    description: str