from app import create_app
from extensions import db
import models

app = create_app()

with app.app_context():
    inspector = db.inspect(db.engine)

    for table_name, table in sorted(db.metadata.tables.items()):
        db_checks = inspector.get_check_constraints(table_name)

        orm_checks = [
            {
                "name": constraint.name,
                "sqltext": str(constraint.sqltext),
            }
            for constraint in table.constraints
            if constraint.__class__.__name__ == "CheckConstraint"
        ]

        if db_checks or orm_checks:
            print(f"\n--- {table_name} ---")
            print("Database CHECK constraints:", db_checks)
            print("ORM CHECK constraints:", orm_checks)

