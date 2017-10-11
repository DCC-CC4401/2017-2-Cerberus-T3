from django.db import models

# Create your models here.


class AnimalType(models.Model):
    type = models.CharField(max_length=50)


class Animal(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey('AnimalType', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='animal_pictures/')
    sex = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    age = models.PositiveSmallIntegerField()
    adoption_time = models.DateField(auto_now_add=True)

