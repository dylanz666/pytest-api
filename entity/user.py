from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    def to_dict(self):
        return self.model_dump()
