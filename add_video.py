#!/usr/bin/env python
"""Add intro video to site configuration"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import SiteConfiguration

config = SiteConfiguration.get_config()
config.hero_video_file = 'videos/intro.mp4'
config.save()

print('✅ Intro video added successfully!')
print('🎥 Video location: media/videos/intro.mp4')
print('🌐 View at: http://localhost:8000')
