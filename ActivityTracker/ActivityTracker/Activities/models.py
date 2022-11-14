from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class person(models.Model):
    netid = models.CharField(max_length=20)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return (self.netid) #Changes the outputs to be a string instead of the object thingy.

class activity(models.Model):
    activity_category = models.CharField(max_length=20)
    activity = models.CharField(max_length=40)
    time_duration = models.DurationField
    personid = models.ForeignKey('Person', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return (self.activity)
