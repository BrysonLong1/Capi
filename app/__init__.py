from flask import Flask
from .routes.health import health_bp

def create_app():
    app = Flask(__name__)
    # you can load env here later if needed
    app.register_blueprint(health_bp)
    return app
