from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

from business.models import Busine
from towns.models import Town
from user_profile.models import UserProfile


class Subsidiary(SafeDeleteModel):

    class Type(models.TextChoices):
        PRINCIPAL = 'Principal', _('Principal')
        SUBSEDE = 'Subsede', _('Subsede')

    class Status(models.TextChoices):
        ACTIVO = 'Activo', _('Activo')
        INACTIVO = 'Inactivo', _('Inactivo')

    busine = models.ForeignKey(Busine, on_delete=models.CASCADE, verbose_name="Empresa")
    name = models.CharField(max_length=80, unique=True, verbose_name="Nombre")
    administrator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Administrador",
                                      related_name="administered_subsidiaries", null=True)
    address = models.CharField(max_length=80, unique=True, verbose_name="Direccion")
    town = models.ForeignKey(Town, on_delete=models.CASCADE, verbose_name="Ciudad")
    phone = models.PositiveBigIntegerField(blank=True, null=True, verbose_name="Telefono")
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.PRINCIPAL, verbose_name="Tipo")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVO, verbose_name="Estado")
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        db_table = 'subsidiary'
        unique_together = ('id',)
        indexes = [
            models.Index(fields=['administrator'], name='fk_sucursal_usuarios1_idx'),
            models.Index(fields=['town'], name='fk_sucursal_municipios1_idx'),
            models.Index(fields=['busine'], name='fk_sucursal_empresa1_idx'),
        ]

    def __str__(self):
        return f"{self.name} - {self.address} - {self.town.name}"
