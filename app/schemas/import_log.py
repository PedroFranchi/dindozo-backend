from pydantic import BaseModel
from datetime import datetime

class ImportLogBase(BaseModel):
    filename: str
    transaction_count: int
    uncategorized_count: int

class ImportLogCreate(ImportLogBase):
    ...

class ImportLogResponse(ImportLogBase):
    id: int
    imported_at: datetime

    class Config:
        from_attributes = True