from pydantic import BaseModel

class TodoUpdate(BaseModel):
    title: str
    description: str
    
class TodoResponse(BaseModel):
    id: str
    title: str
    description: str