
from app import create_app
from extensions import db
import models
from sqlalchemy import UniqueConstraint

app = create_app()

with app.app_context():
    inspector = db.inspect(db.engine)

    for table_name, table in sorted(db.metadata.tables.items()):
        db_unique = inspector.get_unique_constraints(table_name)

        orm_unique = [
            {
                "name": constraint.name,
                "columns": [column.name for column in constraint.columns],
            }
            for constraint in table.constraints
            if isinstance(constraint, UniqueConstraint)
        ]

        orm_unique_columns = [
            column.name
            for column in table.columns
            if column.unique
        ]

        if db_unique or orm_unique or orm_unique_columns:
            print(f"\n--- {table_name} ---")
            print("Database unique constraints:", db_unique)
            print("ORM unique constraints:", orm_unique)
            print("ORM unique columns:", orm_unique_columns)
