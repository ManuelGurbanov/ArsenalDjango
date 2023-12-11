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
    imagen_perfil = models.ImageField(upload_to='jugadores_perfiles/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    equipo_local = models.CharField(max_length=100)
    equipo_visitante = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha}"
