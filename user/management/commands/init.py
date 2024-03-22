import os

from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand
from django.db.models import Q
from dotenv import load_dotenv

load_dotenv()

# from users.models import email_superuser

SUPERUSER_USERNAME = "admin"
SUPERUSER_EMAIL = "admin@admin.com"
SUPERUSER_PASSWORD = "admin"

if not SUPERUSER_PASSWORD:
    raise ImproperlyConfigured("'SUPERUSER_PASSWORD' environment variable is unset")

User = get_user_model()

help_message = f"""
Sets up the DB, creating:
1) superuser with admin rights (Username: {SUPERUSER_USERNAME})
"""


class Command(BaseCommand):
    """
    init: Command to set-up database for the application
    """

    help = help_message

    def handle(self, *args, **kwargs):
        if not User.objects.filter(
            Q(username=SUPERUSER_USERNAME) | Q(email=SUPERUSER_EMAIL)
        ).exists():
            User.objects.create_superuser(
                username=SUPERUSER_USERNAME,
                email=SUPERUSER_EMAIL,
                password=SUPERUSER_PASSWORD,
            )
            print("Super-User Created!")
        print("Set-Up Complete!")