from django.db import models
from django.utils.translation import gettext_lazy as _

class Busine(models.Model):
    class Status(models.TextChoices):
        ACTIVO = 'Activo', _('Activo')
        INACTIVO = 'Inactivo', _('Inactivo')

    name = models.CharField(max_length=80, verbose_name="Nombre")
    nit = models.PositiveIntegerField(unique=True, verbose_name="NIT")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVO, verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creacion", help_text="MM/DD/AAAA")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualización", help_text="MM/DD/AAAA")
    deleted_at = models.DateTimeField(null=True, verbose_name="Eliminacion", help_text="MM/DD/AAAA")

    class Meta:
        db_table = 'business'
        unique_together = ('id',)
        indexes = [
            models.Index(fields=['name'], name='business_name_index'),
        ]
