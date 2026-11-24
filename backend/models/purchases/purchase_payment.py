from sqlalchemy import DateTime, Enum, ForeignKey, Index, Numeric, String, text
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db


class PurchasePayment(db.Model):
    __tablename__ = "purchase_payments"

    __table_args__ = (
        Index("fk_purchase_payments_purchases", "purchase_id"),
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
            name="fk_purchase_payments_purchases",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    amount = db.Column(
        Numeric(12, 2),
        nullable=False,
    )

    payment_method = db.Column(
        Enum(
            "cash",
            "card",
            "bank_transfer",
            "other",
            name="purchase_payment_method",
        ),
        nullable=False,
        server_default="cash",
    )

    payment_date = db.Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    notes = db.Column(
        String(255),
        nullable=True,
    )

    def __repr__(self):
        return f"<PurchasePayment purchase={self.purchase_id}, amount={self.amount}>"
