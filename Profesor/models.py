from django.db import models

# Create your models here.
class Profesor(models.Model):
    CONDICION = (
        ('Masculino','Masculino'),('Femenino','Femenino')
    )

    CONTRATO = (
        ('Contrato','Contrato'),('Nombrado','Nombrado')
    )
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50, choices=CONDICION)
    correo = models.EmailField()
    celular = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=CONTRATO)