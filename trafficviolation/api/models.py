from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    placa_patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return  self.marca + ' ' + self.placa_patente + ' - ' + self.propietario.nombre


class Oficial(models.Model):
    nombre = models.CharField(max_length=100)
    numero_identificatorio = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return  self.nombre + ' ' + self.numero_identificatorio
