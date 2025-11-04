from flask import Blueprint, jsonify

bp = Blueprint("health", __name__)

@bp.get("/")
def root():
    return jsonify(ok=True, service="trovix-capi")

@bp.get("/_health")
def health():
    return jsonify(status="ok")

@bp.get("/healthz")
def healthz():
    return "ok", 200

@bp.get("/readyz")
def readyz():
    # Add real checks (Redis / tokens) if needed
    return "ready", 200

@bp.get("/livez")
def livez():
    return "live", 200
