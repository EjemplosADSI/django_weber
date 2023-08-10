from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Department(models.Model):
    class Region(models.TextChoices):
        CARIBE = 'Caribe', _('Caribe')
        CENTRO_ORIENTE = 'Centro Oriente', _('Centro Oriente')
        CENTRO_SUR = 'Centro Sur', _('Centro Sur')
        EJE_CAFETERO_ANTIOQUIA = 'Eje Cafetero - Antioquia', _('Eje Cafetero - Antioquia')
        LLANO = 'Llano', _('Llano')
        PACIFICO = 'Pacífico', _('Pacífico')

    class Status(models.TextChoices):
        ACTIVO = 'Activo', _('Activo')
        INACTIVO = 'Inactivo', _('Inactivo')

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=90, unique=True, verbose_name="Nombre")
    region = models.CharField(max_length=30, choices=Region.choices, verbose_name="Región")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVO, verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creacion", help_text="MM/DD/AAAA")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualización", help_text="MM/DD/AAAA")
    deleted_at = models.DateTimeField(null=True, verbose_name="Eliminacion", help_text="MM/DD/AAAA")

    class Meta:
        db_table = 'departments'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f"{self.name} - {self.region}"
