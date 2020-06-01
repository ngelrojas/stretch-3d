from django.core.management.base import BaseCommand
from django.db import transaction
from core.user import User


class Command(BaseCommand):
    help = "provide user name and password"

    def success(self, message):
        return self.stdout.write(self.style.SUCCESS(message))

    def warning(self, message):
        return self.stdout.write(self.style.WARNING(message))

    def error(self, message):
        return self.stdout.write(self.style.ERROR(message))

    # def add_arguments(self, parser):
    # parser.add_argument('username', type=str, help='provide username',)
    # parser.add_argument('password', type=str, help='provide password',)

    def handle(self, *args, **options):
        self.warning(
            "if something goes wrong after installations, \n"
            "please use develop environment: \n"
            "docker-compose exec api python manage.py flush"
        )
        # username = options['username']
        # password = options['password']
        with transaction.atomic():
            try:
                User.objects.create_superuser("admin@ngelrojasp.com", "admin2020")
                self.success("admin user created successfully.")
            except Exception:
                self.error("please providde email and password")
