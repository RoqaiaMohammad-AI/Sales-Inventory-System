from sqlalchemy import DateTime, Enum, ForeignKey, Index, Numeric, text
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db
from models.base import TimestampMixin


class SalesReturn(TimestampMixin, db.Model):
    __tablename__ = "sales_returns"

    __table_args__ = (
        Index("fk_sales_returns_sales", "sale_id"),
        Index("fk_sales_returns_users", "user_id"),
        Index("idx_sales_returns_date", "return_date"),
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

    sale_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "sales.id",
            name="fk_sales_returns_sales",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    user_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey(
            "users.id",
            name="fk_sales_returns_users",
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
            name="sales_return_status",
        ),
        nullable=False,
        server_default="draft",
    )

    def __repr__(self):
        return f"<SalesReturn {self.return_number}>"
