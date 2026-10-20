from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Configura el admin para mostrar el rol del usuario."""
    fieldsets = UserAdmin.fieldsets + (
        ("Rol del sistema", {"fields": ("role",)}),
    )
    list_display = ("username", "email", "role", "is_staff")
    list_filter = ("role", "is_staff")