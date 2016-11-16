from django.contrib.gis.db import models


class BaseScore(models.Model):
    name = models.CharField(max_length=50, blank=True)
    geom = models.PointField(blank=True)
    score = models.FloatField(blank=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    """docstring for DataSource"""
    name = models.CharField("Data Source", blank=True, max_length=50)
    base_url = models.URLField("Base Url", blank=True, max_length=255)
    query_string = models.CharField("Query String", blank=True, max_length=255)
    access_token = models.CharField("Access Token", blank=True, max_length=255)
    response_format = models.CharField("Response Format", blank=True, max_length=30)
    request_url = models.URLField("Request URL", blank=True, max_length=500)
    reference_url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        self.request_url = self.base_url + self.query_string + self.response_format + self.access_token
        super(DataSource, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# area = models.IntegerField(blank=True)
# lon = models.FloatField()
# lat = models.FloatField()
# depth = models.FloatField(blank=True)
# waveheight = models.FloatField(blank=True)
# velocity = models.FloatField(blank=True)
# wind_velocity = models.FloatField('Wind Speed', blank=True)
# trib_width = models.FloatField('Tributary Width', blank=True)
# trib_count = models.FloatField('Tributary Count', blank=True)
# fetch = models.FloatField(blank=True)
# ufarea = models.FloatField('Up Flow Area', blank=True)
# tide_range = models.FloatField('Tide Range', blank=True)
# turbidity = models.FloatField(blank=True)
