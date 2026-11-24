from sqlalchemy import ForeignKey, Index
from sqlalchemy.dialects.mysql import BIGINT

from extensions import db
from models.base import TimestampMixin, UpdatedAtMixin


class User(TimestampMixin, UpdatedAtMixin, db.Model):
    __tablename__ = "users"

    __table_args__ = (
        Index("fk_users_roles", "role_id"),
    )

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    role_id = db.Column(
        BIGINT(unsigned=True),
        ForeignKey("roles.id", name="fk_users_roles", onupdate="CASCADE"),
        nullable=False,
    )

    username = db.Column(
        db.String(100),
        nullable=False,
        unique=True,
    )

    full_name = db.Column(
        db.String(150),
        nullable=False,
    )

    email = db.Column(
        db.String(150),
        nullable=True,
        unique=True,
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False,
    )

    is_active = db.Column(
        db.Boolean,
        nullable=False,
        server_default="1",
    )

    def __repr__(self):
        return f"<User {self.username}>"
