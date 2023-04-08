from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    fecha_fundacion = models.DateField()

    def __str__(self):
        return f"Equipo: {self.nombre_equipo} - Region: {self.region} - Fecha de fundación: {self.fecha_fundacion}"


class Jugador(models.Model):
    POSICION_CHOICES = (
        ('g', 'Golero'),
        ('d', 'Defensa'),
        ('m', 'Mediocampista'),
        ('f', 'Delantero'),
    )

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')
    posicion = models.CharField(max_length=1, choices=POSICION_CHOICES)
    titular = models.BooleanField()

    def __str__(self):
        titular_str = "Titular" if self.titular else "Suplente"
        return f"Nombre: {self.nombre} {self.apellido} - Edad: {self.edad} - Equipo: {self.equipo.nombre_equipo} - Posición: {self.get_posicion_display()} - {titular_str}"

class Representante(models.Model):
    nombre = models.CharField(max_length=100)
    sitio_web = models.URLField()
    jugadores_contratados = models.ManyToManyField(Jugador)

    def __str__(self):
        jugadores_str = ", ".join(jugador.nombre for jugador in self.jugadores_contratados.all())
        return f"Nombre: {self.nombre} - Página web: {self.sitio_web} - Jugadores contratados: {jugadores_str}"