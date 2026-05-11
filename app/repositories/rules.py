from sqlalchemy.orm import Session
from app.models.categorization_rules import CategorizationRule
from app.schemas.rules import RuleCreate
from pydantic import  field_validator

def get_all_rules(db: Session):
    return db.query(CategorizationRule).all()

def create_rule(rule: RuleCreate, db: Session):
    optional_rule = db.query(CategorizationRule).filter(CategorizationRule.keyword == rule.keyword).first()
    if optional_rule:
        raise ValueError('A rule with this keyword already exists')
    
    db_rule = CategorizationRule(
        keyword = rule.keyword,
        category_id = rule.category_id
    )
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule


def delete_rule_by_id(db: Session, id: int) -> None:
    rule = db.query(CategorizationRule).filter(CategorizationRule.id == id).first()
    if rule is not None:
        db.delete(rule)
        db.commit()