# scraper_app/models.py
from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField()
    phone_number = models.CharField(max_length=20)
    reviews_count = models.IntegerField()
    reviews_average = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
