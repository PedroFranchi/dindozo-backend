from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional


class TransactionBase(BaseModel):
    date: datetime
    description: str
    amount: float
    type: str
    category_id: Optional[int] = None 
    origin: str
    import_log_id: Optional[int] = None 

    @field_validator('amount')
    @classmethod
    def validate_amount(cls, amount: int):
        if amount == 0:
            raise ValueError('Amount cannot be zero')
        return amount
    
    @field_validator('date')
    @classmethod
    def validate_date(cls, date: datetime):
        if date > datetime.today():
            raise ValueError('Date cannot be in the future')
        return date

    @field_validator('type')
    @classmethod
    def validate_type(cls, type: str):
        if type not in ("income", "expense"):
            raise ValueError('Type must be income or expense')
        return type

class TransactionCreate(TransactionBase):
    ...

class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True