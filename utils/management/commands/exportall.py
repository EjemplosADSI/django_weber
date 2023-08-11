# En el archivo loadall.py
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load all data files'

    def handle(self, *args, **options):
        # Aquí puedes poner los comandos que quieras ejecutar
        call_command('dumpdatautf8', 'departments', '--indent', '4', '--output', 'departments/seed/departments.json')
        call_command('dumpdatautf8', 'towns', '--indent', '4', '--output', 'towns/seed/towns.json')
        call_command('dumpdatautf8', 'business', '--indent', '4', '--output', 'business/seed/business.json')
        call_command('dumpdatautf8', 'subsidiary', '--indent', '4', '--output', 'subsidiary/seed/subsidiary.json')
        call_command('dumpdatautf8', 'auth.User', '--indent', '4', '--output', 'user_profile/seed/auth_user.json')
        call_command('dumpdatautf8', 'user_profile', '--indent', '4', '--output', 'user_profile/seed/user_profile.json')

        # Puedes usar self.stdout.write para mostrar mensajes
        self.stdout.write(self.style.SUCCESS('All data files loaded'))
