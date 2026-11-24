
from app import create_app
from extensions import db
import models

app = create_app()

with app.app_context():
    inspector = db.inspect(db.engine)
    errors = []

    for table_name, table in sorted(db.metadata.tables.items()):
        db_columns = {
            column["name"]: column["nullable"]
            for column in inspector.get_columns(table_name)
        }

        orm_columns = {
            column.name: column.nullable
            for column in table.columns
        }

        mismatches = []

        for column_name, orm_nullable in orm_columns.items():
            db_nullable = db_columns.get(column_name)

            if db_nullable is None or db_nullable != orm_nullable:
                mismatches.append(
                    (column_name, db_nullable, orm_nullable)
                )

        if mismatches:
            errors.append(table_name)
            print(f"\nMismatch: {table_name}")

            for column_name, db_nullable, orm_nullable in mismatches:
                print(
                    f"  {column_name}: "
                    f"Database nullable={db_nullable}, "
                    f"ORM nullable={orm_nullable}"
                )
        else:
            print(f"OK: {table_name}")

    print("\nTables checked:", len(db.metadata.tables))
    print("Tables with nullable mismatches:", len(errors))
    print("All nullable settings match:", len(errors) == 0)
