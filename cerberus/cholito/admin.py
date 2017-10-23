from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, UsuarioAdministrador, UsuarioMunicipalidad, UsuarioNormal, UsuarioONG, TipoDeAnimal,\
    Animal, Abuso, Denuncia


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'sexo', 'edad', 'fechaAdopcion')


class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('estado', 'animal', 'sexo', 'herido', 'fecha', 'localizacion')

admin.site.register(UsuarioAdministrador, UserAdmin)
admin.site.register(UsuarioONG)
admin.site.register(UsuarioNormal)
admin.site.register(UsuarioMunicipalidad)
admin.site.register(Usuario)


admin.site.register(TipoDeAnimal)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Abuso)
admin.site.register(Denuncia, DenunciaAdmin)
