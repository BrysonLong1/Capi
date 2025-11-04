import os, time, urllib.parse, yaml
from flask import Blueprint, request, render_template
from app.config import settings
from app.services.idempotency import make_event_id
from app.services.ga4_mp import send_ga4_event
from app.services.capi_client import send_capi_event

bp = Blueprint("bridge", __name__)

def preserve_params(url: str, req_args) -> str:
    allow = [k.strip() for k in settings.ALLOWED_QUERY_KEYS.split(",")]
    kept = {k: req_args.get(k) for k in allow if req_args.get(k)}
    if kept:
        sep = "&" if ("?" in url) else "?"
        return f"{url}{sep}{urllib.parse.urlencode(kept)}"
    return url

@bp.get("/<slug>")
def bridge(slug: str):
    cfg_path = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "configs", "routes.yml"))
    try:
        with open(cfg_path, "r") as f:
            routes = yaml.safe_load(f) or {}
            dest_url = routes.get(slug)
    except Exception:
        dest_url = None
    if not dest_url:
        return ("Unknown slug", 404)

    ip = request.headers.get("X-Forwarded-For", request.remote_addr or "")
    ua = request.headers.get("User-Agent","")
    event_id = make_event_id(ip, ua, slug)

    # Server-side CAPI InitiateCheckout
    payload = {
        "data": [{
            "event_name": "InitiateCheckout",
            "event_time": int(time.time()),
            "event_source_url": request.url,
            "action_source": "website",
            "event_id": event_id
        }]
    }
    send_capi_event(payload)

    # Server-side GA4 fallback
    send_ga4_event("ic_bridge_hit", {
        "page_location": request.url,
        "utm_source": request.args.get("utm_source", settings.DEFAULT_UTM_SOURCE),
        "utm_medium": request.args.get("utm_medium", settings.DEFAULT_UTM_MEDIUM),
        "utm_campaign": request.args.get("utm_campaign", ""),
        "utm_content": request.args.get("utm_content", ""),
        "utm_term": request.args.get("utm_term", ""),
        "fbclid": request.args.get("fbclid",""),
        "cid": request.args.get("cid",""),
        "evt": request.args.get("evt","")
    })

    final_url = preserve_params(dest_url, request.args)
    return render_template("redirect.html",
        ga4_id=settings.GA4_MEASUREMENT_ID,
        fb_pixel_id=settings.FB_PIXEL_ID,
        page_location=request.url,
        page_referrer=request.referrer or "",
        utm_source=request.args.get("utm_source",""),
        utm_medium=request.args.get("utm_medium",""),
        utm_campaign=request.args.get("utm_campaign",""),
        utm_content=request.args.get("utm_content",""),
        utm_term=request.args.get("utm_term",""),
        fbclid=request.args.get("fbclid",""),
        cid_param=request.args.get("cid",""),
        evt_param=request.args.get("evt",""),
        event_id=event_id,
        final_url=final_url
    )
