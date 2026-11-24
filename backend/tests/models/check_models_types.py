from app import create_app
from extensions import db
import models

app = create_app()

def type_signature(column_type):
    name = column_type.__class__.__name__.upper()

    if name in ("VARCHAR", "STRING"):
        return ("VARCHAR", column_type.length)

    if name == "TEXT":
        return ("TEXT",)

    if name in ("DECIMAL", "NUMERIC"):
        return (
            "DECIMAL",
            column_type.precision,
            column_type.scale,
        )

    if name == "BIGINT":
        return ("BIGINT", getattr(column_type, "unsigned", False))

    if name == "DATETIME":
        return ("DATETIME",)

    if name == "TIMESTAMP":
        return ("TIMESTAMP",)

    if name == "ENUM":
        return ("ENUM", tuple(column_type.enums))

    if name in ("BOOLEAN", "TINYINT"):
        return ("BOOLEAN",)

    return (name,)

with app.app_context():
    inspector = db.inspect(db.engine)
    errors = []

    for table_name, table in sorted(db.metadata.tables.items()):
        db_columns = {
            column["name"]: column
            for column in inspector.get_columns(table_name)
        }

        for column_name, orm_column in table.columns.items():
            db_type = type_signature(
                db_columns[column_name]["type"]
            )
            orm_type = type_signature(orm_column.type)

            if db_type != orm_type:
                errors.append(
                    (table_name, column_name, db_type, orm_type)
                )
                print(f"\nMismatch: {table_name}.{column_name}")
                print("Database:", db_type)
                print("ORM:", orm_type)

    print("\nColumns checked:", sum(
        len(table.columns)
        for table in db.metadata.tables.values()
    ))
    print("Type mismatches:", len(errors))
    print("All column types match:", len(errors) == 0)

