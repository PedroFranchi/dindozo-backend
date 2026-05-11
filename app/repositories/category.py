from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate

def get_all_category(db: Session) -> list[Category]:
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name, color=category.color, icon=category.icon)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category_by_id(db: Session, id: int) -> None:
    category = db.query(Category).filter(Category.id == id).first()
    if category is not None:
        db.delete(category)
        db.commit()