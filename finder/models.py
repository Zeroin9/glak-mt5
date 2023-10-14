from django.db import models

class ATM(models.Model):
    address = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    allDay = models.BooleanField()

    def __str__(self):
        return self.address