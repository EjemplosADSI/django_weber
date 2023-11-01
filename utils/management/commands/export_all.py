# En el archivo export_all.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
import sys


class Command(BaseCommand):
    help = 'Load all data files'

    def export_file(self, name):
        sys.stdout = open(f'{name}/seed/{name}.json', mode='w', encoding='utf8', buffering=1)
        call_command('dumpdatautf8', name, indent=4)
        self.stdout.write(self.style.SUCCESS(f'All data of {name} has export'))

    def handle(self, *args, **options):
        self.export_file("departaments")
        self.export_file("towns")
        self.export_file("business")
        self.export_file("subsidiary")
        self.export_file("user_profile")
