from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional


class RuleBase(BaseModel):
    keyword: str
    category_id: Optional[int] = None

    @field_validator('keyword')
    @classmethod
    def validate_keyword(cls, keyword: str):
        if len(keyword) < 2:
          raise ValueError('Keyword must be at least 2 characters long')
        return keyword

class RuleCreate(RuleBase):
    ...

class RuleResponse(RuleBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True