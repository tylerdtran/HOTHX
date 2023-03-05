# This file contains an explanation for how the SQL database should be structured.
# To update the SQL database after making changes here, type the following commands:
# python manage.py makemigrations
# python manage.py migrate

from django.db import models

# This is the model for the Events table.
class Events(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=2083, default="", unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200, default="")