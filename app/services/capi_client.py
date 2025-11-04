import time, requests
from app.config import settings

FB_URL = f"https://graph.facebook.com/{settings.FB_API_VERSION}/{settings.FB_PIXEL_ID}/events"

def send_capi_event(payload: dict) -> tuple[int, str]:
    headers = {"Content-Type": "application/json"}
    payload["access_token"] = settings.FB_ACCESS_TOKEN
    tries = 0
    while tries < 3:
        try:
            r = requests.post(FB_URL, json=payload, headers=headers, timeout=5)
            if r.status_code >= 500:
                tries += 1
                time.sleep(0.5 * (tries + 1))
                continue
            return r.status_code, r.text
        except Exception:
            tries += 1
            time.sleep(0.5 * (tries + 1))
    return 599, "capi_client: failed after retries"
