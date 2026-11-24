from flask import Flask
from sqlalchemy import text

from config import Config
from extensions import db
from api.inventory.categories import categories_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(categories_bp)

    @app.get("/")
    def home():
        return {
            "message": "Sales & Inventory Management API",
            "status": "running",
        }

    @app.get("/api/health")
    def health():
        try:
            db_version = db.session.execute(
                text("SELECT VERSION()")
            ).scalar()

            database = db.session.execute(
                text("SELECT DATABASE()")
            ).scalar()

            return {
                "status": "ok",
                "database_status": "connected",
                "database": database,
                "database_version": db_version,
            }

        except Exception:
            app.logger.exception("Database health check failed")
            return {
                "status": "error",
                "database_status": "disconnected",
            }, 503

        finally:
            db.session.remove()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
