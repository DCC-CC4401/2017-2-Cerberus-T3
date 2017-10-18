from django.contrib import admin

from .models import TipoDeAnimal, Animal


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'sexo', 'edad', 'fechaAdopcion')


admin.site.register(TipoDeAnimal)
admin.site.register(Animal, AnimalAdmin)