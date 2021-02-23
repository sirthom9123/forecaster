from django.db import models
from django.contrib.auth.models import User
from mapbox_location_field.models import LocationField, AddressAutoHiddenField


class Location(models.Model):
    location = LocationField(null=True, blank=True,
        map_attrs={"style": "mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72", "center": (28.154, -25.7484)})
    address = AddressAutoHiddenField(null=True, blank=True)
    
    def __str__(self):
        return self.location
    
    

class City(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lon = models.CharField(max_length=100, blank=True, null=True)
    temperature = models.CharField(max_length=25)
    humidity = models.CharField(max_length=25, null=True, blank=True)
    wind = models.CharField(max_length=25, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cities'
        
    def __str__(self):
        return self.description
    
    
class ApiKey(models.Model):
    name = models.CharField(max_length=400)
    api_key = models.CharField(max_length=400)
    
    
    def __str__(self):
        return self.name
    