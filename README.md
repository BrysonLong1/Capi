# Trovix CAPI Bridge (GA4 + Meta Pixel/CAPI) — tickets.trovixnights.com

Instagram Ad → **Bridge** → Pixel + CAPI + GA4 → POSH checkout
- Client-side: GA4 `page_view` + `ic_bridge_hit` + Meta Pixel `PageView` + `InitiateCheckout`
- Server-side: Meta CAPI `InitiateCheckout` + GA4 Measurement Protocol `ic_bridge_hit`
- Offline: nightly upload of POSH purchases to Meta as offline `Purchase`

## Quickstart
```bash
# 1) Clone files to /opt/trovix-capi
cp .env.example .env   # fill FB_PIXEL_ID, FB_ACCESS_TOKEN, GA4_MEASUREMENT_ID, GA4_API_SECRET
bash scripts/bootstrap.sh
bash scripts/migrate.sh

# (optional) systemd services
sudo cp systemd/trovix-capi.service /etc/systemd/system/
sudo cp systemd/trovix-capi-worker.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable trovix-capi.service trovix-capi-worker.service
sudo systemctl start trovix-capi.service trovix-capi-worker.service
