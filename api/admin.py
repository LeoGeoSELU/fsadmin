from django.contrib.gis import admin
from .models import BaseScore, DataSource

# Register your models here.
admin.site.register(BaseScore, admin.OSMGeoAdmin)
admin.site.register(DataSource, admin.OSMGeoAdmin)
