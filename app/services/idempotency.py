import hashlib, time

def make_event_id(ip: str, ua: str, slug: str) -> str:
    ts_bucket = int(time.time())
    key = f"{ip}|{ua}|{slug}|{ts_bucket}"
    return hashlib.sha256(key.encode()).hexdigest()
