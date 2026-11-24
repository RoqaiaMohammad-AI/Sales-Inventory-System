from sqlalchemy.dialects.mysql import BIGINT

from extensions import db
from models.base import TimestampMixin


class Category(TimestampMixin, db.Model):
    __tablename__ = "categories"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(120),
        nullable=False,
        unique=True,
    )

    description = db.Column(
        db.Text,
        nullable=True,
    )

    def __repr__(self):
        return f"<Category {self.name}>"
