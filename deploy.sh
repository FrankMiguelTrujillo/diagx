#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "==> Trayendo el codigo nuevo"
git pull --ff-only

echo "==> Reconstruyendo y levantando contenedores"
docker compose up -d --build

echo "==> Aplicando migraciones"
docker compose exec -T api alembic upgrade head

echo "==> Estado final"
docker compose ps