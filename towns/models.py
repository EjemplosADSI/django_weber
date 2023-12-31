from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

from departments.models import Department


class Town(SafeDeleteModel):

    class Status(models.TextChoices):
        ACTIVO = 'Activo', _('Activo')
        INACTIVO = 'Inactivo', _('Inactivo')

    name = models.CharField(max_length=90, verbose_name="Nombre")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Departamento")
    shortened = models.CharField(max_length=40, blank=True, null=True, verbose_name="Acortado")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVO, verbose_name="Estado")
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        db_table = 'towns'
        unique_together = ('id',)
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        indexes = [
            models.Index(fields=['name'], name='municipios_nombre_index'),
            models.Index(fields=['department'], name='mun_depto_id_idx'),
        ]

    def __str__(self):
        return f"{self.name} - {self.department.name}"
