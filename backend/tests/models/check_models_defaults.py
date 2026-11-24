from app import create_app
from extensions import db
import models

app = create_app()

with app.app_context():
    inspector = db.inspect(db.engine)

    for table_name, table in sorted(db.metadata.tables.items()):
        db_columns = {
            column["name"]: column.get("default")
            for column in inspector.get_columns(table_name)
        }

        print(f"\n--- {table_name} ---")

        for column in table.columns:
            orm_default = (
                str(column.server_default.arg)
                if column.server_default is not None
                else None
            )

            db_default = db_columns.get(column.name)

            if db_default is not None or orm_default is not None:
                print(
                    f"{column.name}: "
                    f"Database={db_default!r} | "
                    f"ORM={orm_default!r}"
                )

