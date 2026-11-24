from sqlalchemy.dialects.mysql import BIGINT

from extensions import db
from models.base import TimestampMixin


class Role(TimestampMixin, db.Model):
    __tablename__ = "roles"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )

    description = db.Column(
        db.String(255),
        nullable=True,
    )

    def __repr__(self):
        return f"<Role {self.name}>"
