from sqlalchemy.dialects.mysql import BIGINT

from extensions import db
from models.base import TimestampMixin, UpdatedAtMixin


class StoreSetting(TimestampMixin, UpdatedAtMixin, db.Model):
    __tablename__ = "store_settings"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    store_name = db.Column(
        db.String(180),
        nullable=False,
    )

    phone = db.Column(
        db.String(30),
        nullable=True,
    )

    address = db.Column(
        db.Text,
        nullable=True,
    )

    currency_code = db.Column(
        db.String(10),
        nullable=False,
        server_default="USD",
    )

    language = db.Column(
        db.String(5),
        nullable=False,
        server_default="ar",
    )

    def __repr__(self):
        return f"<StoreSetting {self.store_name}>"
