#!/bin/bash
set -euo pipefail

DB_PASSWORD=$(echo "$DB_PASSWORD" | tr -d '\n')
pg_dump -v "postgresql://postgres:$DB_PASSWORD@$DB_HOST/postgres" >/tmp/backup.sql

datetime=$(date +%Y%m%d%H%M%S)
gcloud storage cp /tmp/backup.sql gs://$BACKUP_TARGET/backup-$datetime.sql