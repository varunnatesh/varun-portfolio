from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Reset admin password to @10varun'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        try:
            admin = User.objects.get(username='admin')
            admin.set_password('@10varun')
            admin.save()
            self.stdout.write(self.style.SUCCESS('✓ Admin password reset to: @10varun'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ Admin user not found'))
