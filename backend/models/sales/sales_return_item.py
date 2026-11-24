from sqlalchemy import Enum, ForeignKey, Index, Numeric
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db


class SalesReturnItem(db.Model):
    __tablename__ = "sales_return_items"

    __table_args__ = (
        Index("fk_sales_return_items_returns", "sales_return_id"),
        Index("fk_sales_return_items_sale_items", "sale_item_id"),
        Index("idx_sales_return_product", "product_id"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    sales_return_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "sales_returns.id",
            name="fk_sales_return_items_returns",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    sale_item_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "sale_items.id",
            name="fk_sales_return_items_sale_items",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    product_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "products.id",
            name="fk_sales_return_items_products",
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

    total = db.Column(
        Numeric(12, 2),
        nullable=False,
    )

    condition_status = db.Column(
        Enum(
            "resellable",
            "damaged",
            name="sales_return_condition",
        ),
        nullable=False,
        server_default="resellable",
    )

    def __repr__(self):
        return f"<SalesReturnItem return={self.sales_return_id}, product={self.product_id}>"
