# gestion/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Medecin, Service
from .models import AppUser
from .models import MessageContact
from .models import Service, ServiceDetail, EffectifService, Medecin, AppUser, MessageContact

class ServiceDetailInline(admin.StackedInline):
    model = ServiceDetail
    extra = 0

class EffectifServiceInline(admin.StackedInline):
    model = EffectifService
    extra = 0

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceDetailInline, EffectifServiceInline]
    list_display = ('nom', 'description')

@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fonction', 'grade', 'service', 'photo')
    list_filter = ('fonction', 'grade', 'service')
    search_fields = ('nom', 'specialite')

class AppUserAdmin(UserAdmin):
    # Champs à afficher dans l'admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'role')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'is_staff', 'is_superuser')}
        ),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(AppUser, AppUserAdmin)


@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi')
    list_filter = ('date_envoi',)
    search_fields = ('nom', 'email', 'sujet', 'message')
