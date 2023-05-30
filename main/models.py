from django.db import models

# Create your models here.
class AboutUs(models.Model):
    description = models.TextField()
    vision = models.CharField(max_length=255)
    mission = models.CharField(max_length=400)
