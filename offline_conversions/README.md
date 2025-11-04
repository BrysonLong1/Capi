# Offline Conversions (POSH → Meta)

1) Export POSH orders to CSV → follow `posh_sample.csv` columns  
2) Configure mapping in `mapping.yml` if your headers differ  
3) Run `bash scripts/offline_upload_cron.sh`

Note: Prefer hashed email/phone if available. Otherwise rely on timestamp + order_id.
