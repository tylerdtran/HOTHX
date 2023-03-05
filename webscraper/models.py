from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=2083, default="", unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200, default="")