from django.db import models

class AirportRouteNode(models.Model):
    route_name = models.CharField(max_length=100)  # group nodes for same route
    airport_code = models.CharField(max_length=10)
    position = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    class Meta:
        unique_together = ('route_name', 'position')
        ordering = ['route_name', 'position']

    def __str__(self):
        return f"{self.route_name} - {self.airport_code} (pos:{self.position}, dur:{self.duration})"
