from sqlalchemy.exc import IntegrityError

from extensions import db
from models import Category


def get_all_categories():
    statement = db.select(Category).order_by(Category.name)
    return db.session.scalars(statement).all()


def get_category_by_id(category_id):
    return db.session.get(Category, category_id)


def create_category(name, description=None):
    category = Category(
        name=name.strip(),
        description=description.strip() if description else None,
    )

    try:
        db.session.add(category)
        db.session.commit()
        return category
    except IntegrityError:
        db.session.rollback()
        raise ValueError("اسم التصنيف مستخدم بالفعل.")


def update_category(category, name, description=None):
    category.name = name.strip()
    category.description = (
        description.strip() if description else None
    )

    try:
        db.session.commit()
        return category
    except IntegrityError:
        db.session.rollback()
        raise ValueError("اسم التصنيف مستخدم بالفعل.")


def delete_category(category):
    try:
        db.session.delete(category)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
