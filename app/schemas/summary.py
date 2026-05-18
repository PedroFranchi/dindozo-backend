from pydantic import BaseModel

class SummaryResponse(BaseModel):
    total_balance: float
    total_income: float
    total_expenses: float
    month: int
    year: int

class MonthlySummaryResponse(BaseModel):
    month: int
    year: int
    income: float
    expenses: float