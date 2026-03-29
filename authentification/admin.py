
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # On ajoute le champ 'role' dans l'interface d'édition
    fieldsets = UserAdmin.fieldsets + (
        ('Informations EPT', {'fields': ('role',)}),
    )
    # On l'ajoute aussi dans le formulaire de création (optionnel)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations EPT', {'fields': ('role',)}),
    )
    # On l'affiche dans la liste de tous les utilisateurs
    list_display = ['username', 'email', 'role', 'is_staff']

admin.site.register(User, CustomUserAdmin)