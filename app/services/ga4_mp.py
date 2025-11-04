import time, uuid, requests
from app.config import settings

def send_ga4_event(event_name: str, params: dict):
    GA4_ID = settings.GA4_MEASUREMENT_ID
    GA4_SECRET = settings.GA4_API_SECRET
    if not (GA4_ID and GA4_SECRET):
        return None
    endpoint = f"https://www.google-analytics.com/mp/collect?measurement_id={GA4_ID}&api_secret={GA4_SECRET}"
    payload = {
        "client_id": str(uuid.uuid4()),
        "timestamp_micros": int(time.time() * 1_000_000),
        "events": [{"name": event_name, "params": params}],
    }
    try:
        r = requests.post(endpoint, json=payload, timeout=5)
        return r.status_code
    except Exception:
        return None
