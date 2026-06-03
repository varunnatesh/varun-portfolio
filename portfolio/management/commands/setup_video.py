from django.core.management.base import BaseCommand
from portfolio.models import SiteConfiguration
from django.core.files import File
from pathlib import Path


class Command(BaseCommand):
    help = 'Set up hero video from deployed media folder'

    def handle(self, *args, **kwargs):
        config = SiteConfiguration.get_config()
        
        # Check if video already configured
        if config.hero_video_file:
            self.stdout.write(self.style.SUCCESS(f'✓ Video already configured: {config.hero_video_file}'))
            return
        
        # Try to set up video from media folder
        video_path = Path('media/videos/intro.mp4')
        
        if not video_path.exists():
            self.stdout.write(self.style.ERROR('✗ Video file not found at media/videos/intro.mp4'))
            return
        
        try:
            with open(video_path, 'rb') as f:
                config.hero_video_file.save('intro.mp4', File(f), save=True)
            self.stdout.write(self.style.SUCCESS('✓ Video file configured successfully!'))
            self.stdout.write(self.style.SUCCESS(f'  Video URL: {config.hero_video_file.url}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Failed to configure video: {e}'))
