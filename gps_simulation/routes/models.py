from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    puntos_interes = models.TextField()  # Puntos turísticos relevantes
    turismo_info = models.TextField(blank=True, null=True)
    actividades = models.TextField(blank=True, null=True)  # Actividades disponibles en la ciudad
    image = models.ImageField(upload_to='cities_images/', blank=True, null=True)  # Campo para la imagen de la ciudad


    def __str__(self):
        return self.name

class Route(models.Model):
    start_city = models.ForeignKey(City, related_name='route_start', on_delete=models.CASCADE)
    end_city = models.ForeignKey(City, related_name='route_end', on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f"{self.start_city} -> {self.end_city} ({self.distance} km)"
