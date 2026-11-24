from sqlalchemy import DateTime, Enum, ForeignKey, Index, Numeric, String, text
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db


class InventoryMovement(db.Model):
    __tablename__ = "inventory_movements"

    __table_args__ = (
        Index("idx_inventory_product_date", "product_id", "movement_date"),
        Index("fk_inventory_movements_users", "user_id"),
        Index("idx_inventory_reference", "reference_type", "reference_id"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    product_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "products.id",
            name="fk_inventory_movements_products",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    user_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "users.id",
            name="fk_inventory_movements_users",
            onupdate="CASCADE",
        ),
        nullable=False,

    )

    movement_type = db.Column(
        Enum(
            "purchase",
            "sale",
            "sales_return",
            "purchase_return",
            "adjustment",
            name="movement_type",
        ),
        nullable=False,
    )

    reference_type = db.Column(
        String(50),
        nullable=True,
    )

    reference_id = db.Column(
        BIGINT(unsigned=True),
        nullable=True,
    )

    quantity = db.Column(
        Numeric(12, 3),
        nullable=False,
    )

    unit_cost = db.Column(
        Numeric(12, 2),
        nullable=True,
        server_default="0.00",
    )

    movement_date = db.Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    notes = db.Column(
        db.Text,
        nullable=True,
    )

    def __repr__(self):
        return f"<InventoryMovement {self.movement_type}: {self.product_id}>"

