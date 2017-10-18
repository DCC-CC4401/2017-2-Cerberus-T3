from django.db import models

sex_choices = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
)


class TipoDeAnimal(models.Model):
    tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tipo de animal"
        verbose_name_plural = 'Tipos de animales'

    def __str__(self):
        return self.tipo


class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey('TipoDeAnimal', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='animal_pictures/')
    sexo = models.CharField(choices=sex_choices, max_length=1)
    edad = models.PositiveSmallIntegerField()
    fechaAdopcion = models.DateField(verbose_name='En adopción desde', auto_now_add=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self):
        return self.nombre
