from flask import Blueprint, jsonify
from app.services.capi_client import send_capi_event

bp = Blueprint("test", __name__)

@bp.get("/_test")
def test():
    payload = {
        "data": [{
            "event_name": "PageView",
            "event_time":  int(__import__("time").time()),
            "event_source_url": "https://tickets.trovixnights.com/_test",
            "action_source": "website"
        }]
    }
    status, text = send_capi_event(payload)
    return jsonify(status=status, response=text)
