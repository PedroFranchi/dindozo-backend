from pydantic import BaseModel, field_validator
from datetime import datetime
import re

class CategoryBase(BaseModel):
    name: str
    color: str
    icon: str

    @field_validator('name')
    @classmethod
    def validate_name(cls, name: str):
        if len(name) < 2:
          raise ValueError('Name must be at least 2 characters long')
        return name
    
    @field_validator('color')
    @classmethod
    def validate_color(cls, color: str):
        hex_pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
        result = bool(re.match(hex_pattern, color))
        if not result:
          raise ValueError('Color must be a valid hex color ex: #22c55e')
        return color
          

class CategoryCreate(CategoryBase):
 ...

class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True