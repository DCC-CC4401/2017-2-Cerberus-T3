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
    descripcion = models.CharField(max_length=600)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self):
        return self.nombre

    def getFechaInicioAdopcion(self):
        mes = self.fechaAdopcion.month
        anho = self.fechaAdopcion.year
        if mes == 1:
            return 'Enero ' + str(anho)
        elif mes == 2:
            return 'Febrero ' + str(anho)
        elif mes == 3:
            return 'Marzo ' + str(anho)
        elif mes == 4:
            return 'Abril ' + str(anho)
        elif mes == 5:
            return 'Mayo ' + str(anho)
        elif mes == 6:
            return 'Junio ' + str(anho)
        elif mes == 7:
            return 'Julio ' + str(anho)
        elif mes == 8:
            return 'Agosto ' + str(anho)
        elif mes == 9:
            return 'Septiembre ' + str(anho)
        elif mes == 10:
            return 'Octubre ' + str(anho)
        elif mes == 11:
            return 'Noviembre ' + str(anho)
        else:
            return 'Diciembre ' + str(anho)


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

    def getAbusos(self):
        abusos = ''
        for abuso in self.abuso.all():
            abusos+= abuso.__str__()+', '
        abusos = abusos[:-2]
        return abusos

    def isHerido(self):
        if self.herido is None:
            return "No especifica"
        elif self.herido:
            return "Si"
        else:
            return "No"

    def getColor(self):
        if self.color == '':
            return 'No especifica'
        return self.color

    def getSexo(self):
        if self.sexo is None:
            return "No especifica"
        elif self.sexo == 'M':
            return 'Macho'
        else:
            return 'Hembra'

class Usuario(AbstractUser):
    pass


class UsuarioNormal(Usuario):
    foto = models.ImageField(upload_to='usuario_pictures/', blank=True)
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
