from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Busine(SafeDeleteModel):

    class Status(models.TextChoices):
        ACTIVO = 'Activo', _('Activo')
        INACTIVO = 'Inactivo', _('Inactivo')

    name = models.CharField(max_length=80, verbose_name="Nombre")
    nit = models.PositiveIntegerField(unique=True, verbose_name="NIT")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVO, verbose_name="Estado")
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        db_table = 'business'
        unique_together = ('id',)
        indexes = [
            models.Index(fields=['name'], name='business_name_index'),
        ]

    def __str__(self):
        return f"{self.name} - {self.nit}"
