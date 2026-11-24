from sqlalchemy import DateTime, Enum, ForeignKey, Index, Numeric, text
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db
from models.base import TimestampMixin


class Purchase(TimestampMixin, db.Model):
    __tablename__ = "purchases"

    __table_args__ = (
        Index("fk_purchases_suppliers", "supplier_id"),
        Index("fk_purchases_users", "user_id"),
        Index("idx_purchases_date", "purchase_date"),
        Index("idx_purchases_status", "status"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    invoice_number = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )

    supplier_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "suppliers.id",
            name="fk_purchases_suppliers",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    user_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "users.id",
            name="fk_purchases_users",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    purchase_date = db.Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    subtotal = db.Column(
        Numeric(12, 2),
        nullable=False,
        server_default="0.00",
    )

    discount = db.Column(
        Numeric(12, 2),
        nullable=False,
        server_default="0.00",
    )

    total_amount = db.Column(
        Numeric(12, 2),
        nullable=False,
        server_default="0.00",
    )

    paid_amount = db.Column(
        Numeric(12, 2),
        nullable=False,
        server_default="0.00",
    )

    status = db.Column(
        Enum(
            "draft",
            "received",
            "cancelled",
            name="purchase_status",
        ),
        nullable=False,
        server_default="draft",
    )

    notes = db.Column(
        db.Text,
        nullable=True,
    )

    def __repr__(self):
        return f"<Purchase {self.invoice_number}>"
