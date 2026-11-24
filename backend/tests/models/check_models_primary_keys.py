from app import create_app
from extensions import db
import models

app = create_app()

with app.app_context():
    inspector = db.inspect(db.engine)
    errors = []

    for table_name, table in sorted(db.metadata.tables.items()):
        db_pk = inspector.get_pk_constraint(table_name)
        db_columns = tuple(db_pk.get("constrained_columns") or ())

        orm_columns = tuple(
            column.name for column in table.primary_key.columns
        )

        if db_columns != orm_columns:
            errors.append(table_name)
            print(f"\nMismatch: {table_name}")
            print("Database PK:", db_columns)
            print("ORM PK:", orm_columns)
        else:
            print(f"OK: {table_name} -> {db_columns}")

    print("\nTables checked:", len(db.metadata.tables))
    print("Tables with PK mismatches:", len(errors))
    print("All primary keys match:", len(errors) == 0)

