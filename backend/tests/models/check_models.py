
from app import create_app
from extensions import db
import models

app = create_app()

with app.app_context():
    inspector = db.inspect(db.engine)
    tables = sorted(db.metadata.tables.keys())
    errors = []

    for table_name in tables:
        db_columns = {
            column["name"]
            for column in inspector.get_columns(table_name)
        }

        orm_columns = set(
            db.metadata.tables[table_name].columns.keys()
        )

        missing_in_orm = db_columns - orm_columns
        missing_in_db = orm_columns - db_columns

        if missing_in_orm or missing_in_db:
            errors.append(table_name)
            print(f"\nMismatch: {table_name}")
            print("Missing in ORM:", sorted(missing_in_orm))
            print("Missing in Database:", sorted(missing_in_db))
        else:
            print(f"OK: {table_name}")

    print("\nTables checked:", len(tables))
    print("Tables with column mismatches:", len(errors))
    print("All columns match:", len(errors) == 0)
