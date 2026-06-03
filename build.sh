#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Starting build process ==="

echo "Installing packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate --no-input

echo "Checking if admin user exists..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'varunnatesh10@gmail.com', 'admin123varun')
    print('Admin user created')
else:
    print('Admin user already exists')
EOF

echo "=== Build complete ==="

