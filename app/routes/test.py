from flask import Blueprint, jsonify

test_bp = Blueprint("test", __name__)

@test_bp.get("/ping")
def ping():
    return jsonify({"pong": True}), 200
