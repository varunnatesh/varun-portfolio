#!/usr/bin/env python
"""Set admin password for Django admin panel"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
admin = User.objects.get(username='admin')
admin.set_password('admin123')  # Change this password after first login!
admin.save()
print('✓ Admin password set to: admin123')
print('⚠ Please change this password after your first login!')
