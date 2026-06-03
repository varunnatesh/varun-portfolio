#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Load initial data automatically (includes Cloudinary video URL)
python manage.py load_initial_data

# Create superuser automatically if it doesn't exist
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'varunnatesh10@gmail.com', 'admin123varun')" | python manage.py shell

