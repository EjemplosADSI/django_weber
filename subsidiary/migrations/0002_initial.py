# Generated by Django 4.2.4 on 2023-08-09 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subsidiary', '0001_initial'),
        ('towns', '0001_initial'),
        ('users', '0001_initial'),
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsidiary',
            name='administrator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administered_subsidiaries', to='users.user', verbose_name='Administrador'),
        ),
        migrations.AddField(
            model_name='subsidiary',
            name='busine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.busine', verbose_name='Empresa'),
        ),
        migrations.AddField(
            model_name='subsidiary',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='towns.town', verbose_name='Ciudad'),
        ),
        migrations.AddIndex(
            model_name='subsidiary',
            index=models.Index(fields=['administrator'], name='fk_sucursal_usuarios1_idx'),
        ),
        migrations.AddIndex(
            model_name='subsidiary',
            index=models.Index(fields=['town'], name='fk_sucursal_municipios1_idx'),
        ),
        migrations.AddIndex(
            model_name='subsidiary',
            index=models.Index(fields=['busine'], name='fk_sucursal_empresa1_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='subsidiary',
            unique_together={('id',)},
        ),
    ]
