
from app import create_app
from extensions import db
import models

app = create_app()

with app.app_context():
    inspector = db.inspect(db.engine)
    errors = []

    for table_name, table in sorted(db.metadata.tables.items()):
        db_fks = inspector.get_foreign_keys(table_name)

        orm_fks = [
            {
                "name": fk.constraint.name,
                "column": fk.parent.name,
                "referred_table": fk.column.table.name,
                "referred_column": fk.column.name,
                "onupdate": fk.onupdate,
                "ondelete": fk.ondelete,
            }
            for fk in table.foreign_keys
        ]

        db_normalized = {
            (
                fk["name"],
                fk["constrained_columns"][0],
                fk["referred_table"],
                fk["referred_columns"][0],
                (fk.get("options") or {}).get("onupdate", "").upper() or None,
                (fk.get("options") or {}).get("ondelete", "").upper() or None,
            )
            for fk in db_fks
        }

        orm_normalized = {
            (
                fk["name"],
                fk["column"],
                fk["referred_table"],
                fk["referred_column"],
                fk["onupdate"].upper() if fk["onupdate"] else None,
                fk["ondelete"].upper() if fk["ondelete"] else None,
            )
            for fk in orm_fks
        }

        if db_normalized != orm_normalized:
            errors.append(table_name)
            print(f"\nMismatch: {table_name}")
            print("Database:", db_normalized)
            print("ORM:", orm_normalized)
        else:
            print(f"OK: {table_name} ({len(db_normalized)} foreign keys)")

    print("\nTables checked:", len(db.metadata.tables))
    print("Tables with FK mismatches:", len(errors))
    print("All foreign keys match:", len(errors) == 0)
