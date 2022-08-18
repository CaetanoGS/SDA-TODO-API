from pydantic import BaseModel

class TodoUpdateSchema(BaseModel):
    title: str
    description: str