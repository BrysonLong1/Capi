#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
. .venv/bin/activate
python - <<'PY'
from sqlalchemy import create_engine, text
import os
db = os.getenv("DATABASE_URL", "sqlite:///bridge.db")
engine = create_engine(db)
with engine.begin() as c:
    c.execute(text("""
    CREATE TABLE IF NOT EXISTS bridge_events (
        event_id TEXT PRIMARY KEY,
        ts INTEGER,
        slug TEXT,
        dest_url TEXT,
        ip_hash TEXT,
        ua_hash TEXT,
        utm_source TEXT,
        utm_medium TEXT,
        utm_campaign TEXT,
        utm_content TEXT,
        utm_term TEXT,
        click_ids TEXT,
        status TEXT
    );
    """))
print("DB migrate OK")
PY
