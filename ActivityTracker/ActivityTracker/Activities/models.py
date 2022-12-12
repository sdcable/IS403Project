from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class person(models.Model):
    netid = models.CharField(max_length=20)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=13, blank=True)
    description = models.CharField(null=True, blank=True, max_length=250)
    instagram = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return (self.netid) #Changes the outputs to be a string instead of the object thingy.

class activity(models.Model):
    activity_category = models.CharField(max_length=50, null=True, blank=True)
    activity_title = models.CharField(max_length=100, null=True, blank=True)
    activity_description = models.CharField(max_length=200, null=True, blank=True)
    time_duration = models.DurationField
    personid = models.ForeignKey('Person', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return (self.personid.netid + ", " + self.activity_category + ", " + self.activity_title)
