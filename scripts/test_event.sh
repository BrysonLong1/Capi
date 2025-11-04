#!/usr/bin/env bash
set -euo pipefail
BASE="${BASE:-https://tickets.trovixnights.com}"
SLUG="${1:-tally-event}"
PARAMS="utm_source=meta&utm_medium=paid-social&utm_campaign=fsu_pop_up&utm_content=teaser_reel&cid=tallahassee&evt=fsu_homecoming&fbclid=fb.12345"
curl -sS -I "$BASE/$SLUG?$PARAMS" | awk '/^HTTP|Location:/ {print}'
