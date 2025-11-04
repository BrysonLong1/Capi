import os, csv, time, requests
from datetime import datetime
from app.config import settings

# Demo uploader: sends offline "Purchase" to Pixel events endpoint with action_source=offline
# For production: consider the Conversions API for Offline Events (same endpoint).

def iso_to_epoch(s):
    try:
        return int(datetime.fromisoformat(s.replace('Z','+00:00')).timestamp())
    except Exception:
        try:
            return int(s)
        except Exception:
            return int(time.time())

def main():
    csv_path = os.getenv("POSH_CSV", "offline_conversions/posh_sample.csv")
    if not os.path.exists(csv_path):
        print("No CSV found:", csv_path); return
    rows = list(csv.DictReader(open(csv_path)))
    events = []
    for r in rows:
        ev = {
            "event_name": "Purchase",
            "event_time": iso_to_epoch(r.get("purchased_at","")),
            "action_source": "offline",
            "custom_data": {"value": float(r.get("amount","0") or 0.0), "currency": "USD"},
            "user_data": {}
        }
        em = (r.get("email_hash") or "").strip()
        ph = (r.get("phone_hash") or "").strip()
        if em: ev["user_data"]["em"] = [em]
        if ph: ev["user_data"]["ph"] = [ph]
        events.append(ev)

    payload = {"data": events, "access_token": settings.FB_ACCESS_TOKEN }
    url = f"https://graph.facebook.com/{settings.FB_API_VERSION}/{settings.FB_PIXEL_ID}/events"
    try:
        r = requests.post(url, json=payload, timeout=10)
        print("Upload status:", r.status_code, r.text[:300])
    except Exception as e:
        print("Upload error:", e)

if __name__ == "__main__":
    main()
