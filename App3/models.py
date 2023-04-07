from django.db import models

# Create your models here.
class Jugador(models.Model):
    
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    equipo = models.CharField(max_length=200, default="Sin Equipo")
    titular = models.BooleanField()


    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido} - Edad: {self.edad} - Posición: {self.posicion})"
        
class Equipo(models.Model):
    
    nombre_equipo = models.CharField(max_length=50)
    jugadores = models.CharField(max_length=200, default='')
    fecha_de_transferencia = models.DateField()

    def __str__(self):
        return f"Equipo: {self.nombre_equipo} - Jugadores: {self.jugadores} - Fecha de transferencia: {self.fecha_de_transferencia}"

class Representante(models.Model):
    
    nombre = models.CharField(max_length=100)
    sitio_web = models.URLField()
    contrato_total = models.BooleanField()
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.nombre} - Página web: {self.sitio_web} - Posee el contrato total: {self.contrato_total}"

    