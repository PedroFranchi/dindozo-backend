from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.models.categorization_rules import CategorizationRule

def categorize(db: Session, transactions: list[Transaction]):
    rules = db.query(CategorizationRule).all()
    
    for transaction in transactions:
        for rule in rules:
            if rule.keyword.lower() in transaction['description'].lower():
                transaction['category_id'] = rule.category_id
                break
        else:
            transaction['category_id'] = None
    return transactions