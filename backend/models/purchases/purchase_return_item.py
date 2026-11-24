from sqlalchemy import ForeignKey, Index, Numeric
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db


class PurchaseReturnItem(db.Model):
    __tablename__ = "purchase_return_items"

    __table_args__ = (
        Index("fk_purchase_return_items_returns", "purchase_return_id"),
        Index("fk_purchase_return_items_purchase_items", "purchase_item_id"),
        Index("idx_purchase_return_product", "product_id"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    purchase_return_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "purchase_returns.id",
            name="fk_purchase_return_items_returns",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    purchase_item_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "purchase_items.id",
            name="fk_purchase_return_items_purchase_items",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    product_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "products.id",
            name="fk_purchase_return_items_products",
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
        return (
            f"<PurchaseReturnItem "
            f"return={self.purchase_return_id}, "
            f"product={self.product_id}>"
        )
