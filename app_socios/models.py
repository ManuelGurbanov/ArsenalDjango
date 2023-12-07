from django.db import models

class Socio(models.Model):
    nombre  =  models.CharField(max_length=200)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
    

class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre  =  models.CharField(max_length=50)
    edad = models.IntegerField()
    posicion  =  models.CharField(max_length=3)

    def __str__(self):
        return self.nombre
    