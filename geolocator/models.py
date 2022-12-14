from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import django.utils.timezone

# Create your models here.
class ImagesDB(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    description = models.TextField(default='Fill')
    date_added = models.DateField(default=django.utils.timezone.now)
    image_lat = models.FloatField(default=0)
    image_long = models.FloatField(default=0)
    image_lat_long = models.TextField(default="LatLng(0, 0)")
    location = PlainLocationField(based_fields=['city'],default=('60.45,22.26'), zoom=7)