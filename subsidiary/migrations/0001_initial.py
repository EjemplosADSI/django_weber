# Generated by Django 4.2.4 on 2023-08-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subsidiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Nombre')),
                ('address', models.CharField(max_length=80, unique=True, verbose_name='Direccion')),
                ('phone', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Telefono')),
                ('type', models.CharField(choices=[('Principal', 'Principal'), ('Subsede', 'Subsede')], default='Principal', max_length=10, verbose_name='Tipo')),
                ('status', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado')),
            ],
            options={
                'db_table': 'subsidiary',
            },
        ),
    ]
