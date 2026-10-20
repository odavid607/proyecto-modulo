from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Usuario extendido con roles del sistema."""
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        GESTOR = "GESTOR", "Gestor"
        USUARIO = "USUARIO", "Usuario"
        VISITANTE = "VISITANTE", "Visitante"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.VISITANTE,
        help_text="Rol que determina los permisos del usuario."
    )

    # ESTAS DOS LÍNEAS ARREGLAN EL CHOQUE DE ERRORES
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_set', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions_set', blank=True
    )

    def is_admin_role(self):
        return self.role == self.Role.ADMIN or self.is_superuser