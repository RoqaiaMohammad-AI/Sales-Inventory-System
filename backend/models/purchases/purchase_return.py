from sqlalchemy import DateTime, Enum, ForeignKey, Index, Numeric, text
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db
from models.base import TimestampMixin


class PurchaseReturn(TimestampMixin, db.Model):
    __tablename__ = "purchase_returns"

    __table_args__ = (
        Index("fk_purchase_returns_purchases", "purchase_id"),
        Index("fk_purchase_returns_users", "user_id"),
        Index("idx_purchase_returns_date", "return_date"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    return_number = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )

    purchase_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "purchases.id",
            name="fk_purchase_returns_purchases",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    user_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "users.id",
            name="fk_purchase_returns_users",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    return_date = db.Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    total_amount = db.Column(
        Numeric(12, 2),
        nullable=False,
        server_default="0.00",
    )

    reason = db.Column(
        db.Text,
        nullable=True,
    )

    status = db.Column(
        Enum(
            "draft",
            "confirmed",
            "cancelled",
            name="purchase_return_status",
        ),
        nullable=False,
        server_default="draft",
    )

    def __repr__(self):
        return f"<PurchaseReturn {self.return_number}>"
