from django.db import models

# Create your models here.
class Alumno(models.Model):
    CONDICION = (
        ('Masculino','Masculino'),('Femenino','Femenino')
    )

    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50, choices=CONDICION)
    correo = models.EmailField()