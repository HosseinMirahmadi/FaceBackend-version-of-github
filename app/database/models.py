
from pydantic import BaseModel
from datetime import datetime

class Ping(BaseModel):
    path: str
    status: str
    created_at: datetime = None
    updated_at: datetime = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

class Faces(BaseModel):
    name: str
