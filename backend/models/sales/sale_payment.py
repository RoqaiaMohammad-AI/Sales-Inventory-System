from sqlalchemy import DateTime, Enum, ForeignKey, Index, Numeric, String, text
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db


class SalePayment(db.Model):
    __tablename__ = "sale_payments"

    __table_args__ = (
        Index("fk_sale_payments_sales", "sale_id"),
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
            name="fk_sale_payments_sales",
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
            name="sale_payment_method",
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
        return f"<SalePayment sale={self.sale_id}, amount={self.amount}>"
