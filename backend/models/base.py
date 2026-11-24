from sqlalchemy import FetchedValue, func
from sqlalchemy.dialects.mysql import TIMESTAMP

from extensions import db


Base = db.Model


class TimestampMixin:
    created_at = db.Column(
        TIMESTAMP(),
        nullable=False,
        server_default=func.current_timestamp(),
    )


class UpdatedAtMixin:
    updated_at = db.Column(
        TIMESTAMP(),
        nullable=False,
        server_default=func.current_timestamp(),
        server_onupdate=FetchedValue(),
    )
