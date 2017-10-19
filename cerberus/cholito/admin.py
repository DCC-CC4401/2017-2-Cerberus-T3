from django.contrib import admin

from .models import TipoDeAnimal, Animal, Abuso, Denuncia


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'sexo', 'edad', 'fechaAdopcion')


class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('estado', 'animal', 'sexo', 'herido', 'fecha', 'localizacion')

admin.site.register(TipoDeAnimal)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Abuso)
admin.site.register(Denuncia, DenunciaAdmin)
