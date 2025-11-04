from flask import Flask
from app.config import settings
from app.routes.health import bp as health_bp
from app.routes.bridge import bp as bridge_bp
from app.routes.test import bp as test_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings.SECRET_KEY

    app.register_blueprint(health_bp)
    app.register_blueprint(bridge_bp)
    app.register_blueprint(test_bp)

    return app

app = create_app()
