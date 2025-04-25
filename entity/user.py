from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert the User instance to a dictionary."""
        return self.dict()

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        """Create a User instance from a dictionary."""
        return cls(**data)
