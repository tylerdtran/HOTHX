# This file contains an explanation for how the SQL database should be structured.
# To update the SQL database after making changes here, type the following commands:
# python manage.py makemigrations
# python manage.py migrate

from django.db import models

# This is the model for the Events table.
class Events(models.Model):
    eventname = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    link = models.CharField(max_length=2083)
    date_and_time = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="")
    placeid = models.CharField(max_length=200, default="")

    # def __str__(self):
    #     return self.eventname
    # def __repr__(self):
    #     return self.eventname