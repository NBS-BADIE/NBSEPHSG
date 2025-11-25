import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hopital.settings')
django.setup()

from django.core.management import call_command

print("📦 Création et application des migrations sur Render...")
call_command('makemigrations')
call_command('migrate')
print("✅ Migrations appliquées avec succès sur Render !")
