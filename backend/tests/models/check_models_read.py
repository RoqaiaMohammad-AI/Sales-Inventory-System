
from app import create_app
from extensions import db
import models

app = create_app()

with app.app_context():
    for table_name, table in sorted(db.metadata.tables.items()):
        db.session.execute(
            db.select(table).limit(1)
        ).fetchall()

        print(f"OK: {table_name}")

    print("\nAll 18 ORM models passed read tests.")
    db.session.remove()
