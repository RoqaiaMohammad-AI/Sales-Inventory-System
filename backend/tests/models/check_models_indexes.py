from app import create_app
from extensions import db
import models

app = create_app()

with app.app_context():
    inspector = db.inspect(db.engine)
    errors = []

    for table_name, table in sorted(db.metadata.tables.items()):
        db_indexes = {
            (index["name"], tuple(index["column_names"]))
            for index in inspector.get_indexes(table_name)
            if not index.get("unique", False)
        }

        orm_indexes = {
            (index.name, tuple(column.name for column in index.columns))
            for index in table.indexes
            if not index.unique
        }

        if db_indexes != orm_indexes:
            errors.append(table_name)
            print(f"\nMismatch: {table_name}")
            print("Database:", db_indexes)
            print("ORM:", orm_indexes)
            print("Database only:", db_indexes - orm_indexes)
            print("ORM only:", orm_indexes - db_indexes)
        else:
            print(f"OK: {table_name} ({len(db_indexes)} indexes)")

    print("\nTables checked:", len(db.metadata.tables))
    print("Tables with mismatches:", len(errors))
    print("All non-unique indexes match:", len(errors) == 0)

