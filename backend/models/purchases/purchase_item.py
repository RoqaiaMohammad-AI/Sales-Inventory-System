from sqlalchemy import ForeignKey, Index, Numeric
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db


class PurchaseItem(db.Model):
    __tablename__ = "purchase_items"

    __table_args__ = (
        Index("fk_purchase_items_purchases", "purchase_id"),
        Index("idx_purchase_items_product", "product_id"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    purchase_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "purchases.id",
            name="fk_purchase_items_purchases",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    product_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "products.id",
            name="fk_purchase_items_products",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    quantity = db.Column(
        Numeric(12, 3),
        nullable=False,
    )

    unit_cost = db.Column(
        Numeric(12, 2),
        nullable=False,
    )

    total = db.Column(
        Numeric(12, 2),
        nullable=False,
    )

    def __repr__(self):
        return f"<PurchaseItem purchase={self.purchase_id}, product={self.product_id}>"
