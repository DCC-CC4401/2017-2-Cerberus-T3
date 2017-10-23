from django.contrib.auth.models import AbstractUser
from django.db import models

sexo_opciones = (
    (None, 'No especifica'),
    ('M', 'Masculino'),
    ('F', 'Femenino')
)


def crear_tipo_de_animal_por_defecto():
    return TipoDeAnimal.objects.get_or_create(tipo='Otro')


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
    sexo = models.CharField(choices=sexo_opciones, max_length=1)
    edad = models.PositiveSmallIntegerField()
    fechaAdopcion = models.DateField(verbose_name='En adopción desde', auto_now_add=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self):
        return self.nombre


class Abuso (models.Model):
    tipo = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Abuso'
        verbose_name_plural = 'Abusos'

    def __str__(self):
        return self.tipo


class Denuncia (models.Model):
    estado_opciones = (
        ('Reportada', 'Reportada'),
        ('Consolidada', 'Consolidada'),
        ('Verificada', 'Verificada'),
        ('Cerrada', 'Cerrada'),
        ('Desechada', 'Desechada')
    )

    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(choices=estado_opciones, max_length=15, default='Reportada')
    abuso = models.ManyToManyField(Abuso, blank=True)
    localizacion = models.CharField(max_length=300, verbose_name='Lugar de la denuncia')  # Dummy
    animal = models.ForeignKey('TipoDeAnimal', verbose_name='Tipo de animal', default=crear_tipo_de_animal_por_defecto)
    sexo = models.CharField(choices=sexo_opciones, max_length=1, blank=True)
    color = models.CharField(max_length=50, blank=True)
    herido = models.NullBooleanField(default=None)

    class Meta:
        verbose_name = 'Denuncia'
        verbose_name_plural = 'Denuncias'

    def __str__(self):
        return self.estado


class Usuario(AbstractUser):
    pass


class UsuarioNormal(Usuario):
    class Meta:
        verbose_name = 'Persona Natural'
        verbose_name_plural = 'Personas Naturales'


class UsuarioMunicipalidad(Usuario):
    foto = models.ImageField(upload_to='municipalidad_pictures/', blank=True)

    class Meta:
        verbose_name = 'Representante Municipal'
        verbose_name_plural = 'Representantes Municipales'


class UsuarioONG(Usuario):
    foto = models.ImageField(upload_to='ong_pictures/', blank=True)

    class Meta:
        verbose_name = 'Representante ONG'
        verbose_name_plural = 'Representantes ONG'


class UsuarioAdministrador(Usuario):
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
