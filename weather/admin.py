from django.contrib import admin
from .models import City, Location, ApiKey
from mapbox_location_field.admin import MapAdmin 


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['owner', 'lat', 'lon', 'temperature', 'humidity', 'wind', 'description', 'created']
    list_filter = ['created', ]

class ApikeyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(ApiKey, ApikeyAdmin)
admin.site.register(Location, MapAdmin)