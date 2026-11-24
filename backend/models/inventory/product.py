from sqlalchemy import CheckConstraint, ForeignKey, Index, Numeric
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db
from models.base import TimestampMixin, UpdatedAtMixin


class Product(TimestampMixin, UpdatedAtMixin, db.Model):
    __tablename__ = "products"

    __table_args__ = (
        CheckConstraint(
            "purchase_price >= 0 AND selling_price >= 0",
            name="chk_products_prices",
        ),
        CheckConstraint(
            "current_stock >= 0 AND reorder_level >= 0",
            name="chk_products_stock",
        ),
        Index("idx_products_name", "name"),
        Index("fk_products_categories", "category_id"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    category_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "categories.id",
            name="fk_products_categories",
            ondelete="SET NULL",
            onupdate="CASCADE",
        ),
        nullable=True,
    )

    sku = db.Column(
        db.String(100),
        nullable=False,
        unique=True,
    )

    barcode = db.Column(
        db.String(100),
        nullable=True,
        unique=True,
    )

    name = db.Column(
        db.String(180),
        nullable=False,
        index=False,
    )

    description = db.Column(
        db.Text,
        nullable=True,
    )

    purchase_price = db.Column(
        Numeric(12, 2),
        nullable=False,
        server_default="0.00",
    )

    selling_price = db.Column(
        Numeric(12, 2),
        nullable=False,
        server_default="0.00",
    )

    current_stock = db.Column(
        Numeric(12, 3),
        nullable=False,
        server_default="0.000",
    )

    reorder_level = db.Column(
        Numeric(12, 3),
        nullable=False,
        server_default="0.000",
    )

    is_active = db.Column(
        db.Boolean,
        nullable=False,
        server_default="1",
    )

    def __repr__(self):
        return f"<Product {self.sku}: {self.name}>"
