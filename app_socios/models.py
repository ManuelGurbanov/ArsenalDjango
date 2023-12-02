from django.db import models

class Socio(models.Model):
    nombre  =  models.CharField(max_length=200)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
    