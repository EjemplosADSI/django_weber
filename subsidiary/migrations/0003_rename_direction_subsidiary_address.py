# Generated by Django 4.2.4 on 2023-08-10 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subsidiary', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsidiary',
            old_name='direction',
            new_name='address',
        ),
    ]
