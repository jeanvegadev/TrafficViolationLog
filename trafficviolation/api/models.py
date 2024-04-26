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
        return self.marca + ' ' + \
               self.placa_patente + ' - ' +\
               self.propietario.nombre


class Oficial(models.Model):
    nombre = models.CharField(max_length=100)
    numero_identificatorio = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre + ' ' + self.numero_identificatorio


class Infraccion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    oficial = models.ForeignKey(Oficial, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    motivo = models.CharField(max_length=1000)

    def __str__(self):
        return self.vehiculo.placa_patente + ' ' + self.motivo


class AccessToken(models.Model):
    oficial = models.OneToOneField(Oficial, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
