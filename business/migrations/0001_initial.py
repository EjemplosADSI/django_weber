# Generated by Django 4.2.4 on 2023-08-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Busine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('nit', models.PositiveIntegerField(unique=True, verbose_name='NIT')),
                ('status', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado')),
            ],
            options={
                'db_table': 'business',
                'indexes': [models.Index(fields=['name'], name='business_name_index')],
                'unique_together': {('id',)},
            },
        ),
    ]
