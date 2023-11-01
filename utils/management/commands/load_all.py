# En el archivo load_all.py
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load all data files'

    def handle(self, *args, **options):
        # Aquí puedes poner los comandos que quieras ejecutar
        call_command('loaddatautf8', 'departments/seed/departments.json')
        call_command('loaddatautf8', 'towns/seed/towns.json')
        call_command('loaddatautf8', 'business/seed/business.json')
        call_command('loaddatautf8', 'subsidiary/seed/subsidiary.json')
        call_command('loaddatautf8', 'user_profile/seed/auth_user.json')
        call_command('loaddatautf8', 'user_profile/seed/user_profile.json')
        # Puedes usar self.stdout.write para mostrar mensajes
        self.stdout.write(self.style.SUCCESS('All data files loaded'))
