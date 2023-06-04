from django.db import models

# Create your models here.

class Program(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/programs-pics/')

    def __str__(self) -> str:
        return self.title

class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/activity-pics/')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class AboutUs(models.Model):
    description = models.TextField()
    vision = models.CharField(max_length=255)
    mission = models.CharField(max_length=400)
