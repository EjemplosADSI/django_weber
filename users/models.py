from django.db import models
from django.utils.translation import gettext_lazy as _

from subsidiary import models as subsidiary_models
from towns.models import Town


class User(models.Model):
    class Gender(models.TextChoices):
        FEMENINO = 'Femenino', _('Femenino')
        MASCULINO = 'Masculino', _('Masculino')
        OTRO = 'Otro', _('Otro')

    class DocumentType(models.TextChoices):
        CEDULA_DE_CIUDADANIA = 'Cédula de Ciudadanía', _('Cédula de Ciudadanía')
        CEDULA_DE_EXTRANJERIA = 'Cédula de Extranjería', _('Cédula de Extranjería')
        PASAPORTE = 'Pasaporte', _('Pasaporte')
        REGISTRO_CIVIL = 'Registro Civil', _('Registro Civil')
        TARJETA_DE_IDENTIDAD = 'Tarjeta de Identidad', _('Tarjeta de Identidad')

    class Role(models.TextChoices):
        FEMENINO = 'Femenino', _('Femenino')
        EMPLEADO = 'Empleado', _('Empleado')
        CLIENTE = 'Cliente', _('Cliente')
        PROVEEDOR = 'Proveedor', _('Proveedor')

    class Status(models.TextChoices):
        ACTIVO = 'Activo', _('Activo')
        INACTIVO = 'Inactivo', _('Inactivo')

    name = models.CharField(max_length=60, verbose_name="Nombres")
    last_name = models.CharField(max_length=60, verbose_name="Apellidos")
    email = models.EmailField(unique=True, verbose_name="Correo")
    email_verified_at = models.DateTimeField(blank=True, null=True, verbose_name="Verificacion Email")
    password = models.CharField(max_length=256, blank=True, null=True, verbose_name="Contraseña")
    photo = models.CharField(max_length=45, default='default_user.jpg', verbose_name="Foto")
    gender = models.CharField(max_length=10, choices=Gender.choices, blank=True, null=True, default=Gender.MASCULINO, verbose_name="Genero")
    document_type = models.CharField(max_length=25, choices=DocumentType.choices, default=DocumentType.CEDULA_DE_CIUDADANIA, verbose_name="Tipo Documento")
    document = models.PositiveBigIntegerField(unique=True, verbose_name="Documento")
    phone = models.PositiveBigIntegerField(blank=True, null=True, verbose_name="Telefono")
    address = models.CharField(max_length=70, blank=True, null=True, verbose_name="Direccion")
    town = models.ForeignKey(Town, on_delete=models.CASCADE, verbose_name="Ciudad")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Nacimiento")
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.CLIENTE, verbose_name="Rol")
    subsidiary = models.ForeignKey("subsidiary.Subsidiary", on_delete=models.CASCADE, verbose_name="Sucursal")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVO, verbose_name="Estado")
    remember_token = models.CharField(max_length=100, blank=True, null=True, verbose_name="Token")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creacion", help_text="MM/DD/AAAA")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualización", help_text="MM/DD/AAAA")
    deleted_at = models.DateTimeField(null=True, verbose_name="Eliminacion", help_text="MM/DD/AAAA")

    class Meta:
        db_table = 'users'
        unique_together = ('id',)
        indexes = [
            models.Index(fields=['name'], name='users_name_index'),
            models.Index(fields=['last_name'], name='users_last_name_index'),
            models.Index(fields=['town'], name='fk_usuarios_municipios1_idx'),
            models.Index(fields=['subsidiary'], name='fk_usuarios_sucursal1_idx'),
        ]
