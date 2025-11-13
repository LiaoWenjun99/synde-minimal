#!/bin/bash
# ============================================
# SynDe Minimal Deployment Script
# ============================================

set -e

echo "📦 Pulling latest version from GitHub..."
cd /home/ubuntu/synde-minimal
git fetch origin main
git reset --hard origin/main

echo "🐍 Activating virtual environment..."
source /home/ubuntu/synde-minimal/venv/bin/activate

echo "🧱 Applying migrations..."
python manage.py migrate --noinput

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

echo "🔁 Restarting Gunicorn and Nginx..."
sudo systemctl restart gunicorn
sudo systemctl restart nginx

echo "✅ Deployment complete! Visit http://$(curl -s ifconfig.me)/ to verify."
