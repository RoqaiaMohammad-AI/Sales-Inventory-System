from sqlalchemy import ForeignKey, Index, Numeric
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db


class SaleItem(db.Model):
    __tablename__ = "sale_items"

    __table_args__ = (
        Index("fk_sale_items_sales", "sale_id"),
        Index("idx_sale_items_product", "product_id"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    sale_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "sales.id",
            name="fk_sale_items_sales",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    product_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "products.id",
            name="fk_sale_items_products",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    quantity = db.Column(
        Numeric(12, 3),
        nullable=False,
    )

    unit_price = db.Column(
        Numeric(12, 2),
        nullable=False,
    )

    unit_cost = db.Column(
        Numeric(12, 2),
        nullable=False,
        server_default="0.00",
    )

    discount = db.Column(
        Numeric(12, 2),
        nullable=False,
        server_default="0.00",
    )

    total = db.Column(
        Numeric(12, 2),
        nullable=False,
    )

    def __repr__(self):
        return f"<SaleItem sale={self.sale_id}, product={self.product_id}>"
