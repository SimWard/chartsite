from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from chartsite.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from chartsite.main.routes import main
        from chartsite.charts.routes import charts
        app.register_blueprint(main)
        app.register_blueprint(charts)

        db.create_all()

        return app
