from sqlalchemy import Index
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db
from models.base import TimestampMixin


class Supplier(TimestampMixin, db.Model):
    __tablename__ = "suppliers"

    __table_args__ = (
        Index("idx_suppliers_name", "name"),
        Index("idx_suppliers_phone", "phone"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(150),
        nullable=False,
    )

    phone = db.Column(
        db.String(30),
        nullable=True,
    )

    email = db.Column(
        db.String(150),
        nullable=True,
    )

    address = db.Column(
        db.Text,
        nullable=True,
    )

    def __repr__(self):
        return f"<Supplier {self.name}>"
