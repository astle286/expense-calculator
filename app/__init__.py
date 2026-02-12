from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter

db = SQLAlchemy()

# Prometheus metrics setup
metrics = PrometheusMetrics.for_app_factory()
expenses_added_total = Counter("expenses_added_total", "Total number of expenses added")

def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class or 'config.Config')

    db.init_app(app)
    metrics.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
