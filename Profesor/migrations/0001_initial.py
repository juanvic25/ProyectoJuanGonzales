# Generated by Django 4.1.4 on 2023-01-13 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profesor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("edad", models.IntegerField()),
                (
                    "sexo",
                    models.CharField(
                        choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")],
                        max_length=50,
                    ),
                ),
                ("correo", models.EmailField(max_length=254)),
                ("celular", models.IntegerField()),
                (
                    "tipo",
                    models.CharField(
                        choices=[("Contrato", "Contrato"), ("Nombrado", "Nombrado")],
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
