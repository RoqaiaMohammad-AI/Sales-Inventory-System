from app import create_app
from extensions import db
import models

app = create_app()

with app.app_context():
    for table_name, table in sorted(db.metadata.tables.items()):
        for column in table.columns:
            if column.server_onupdate is not None:
                print(
                    f"{table_name}.{column.name}: "
                    f"server_onupdate={column.server_onupdate}"
                )

