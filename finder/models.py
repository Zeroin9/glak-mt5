from django.db import models

class ATM(models.Model):
    address = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    allDay = models.BooleanField()

    def __str__(self):
        return self.address

class Office(models.Model):
    salePointName = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    status = models.CharField(max_length=256)
    rko = models.BooleanField()
    officeType = models.BooleanField()
    officeTypeAdditional = models.CharField(max_length=256, null=True)
    salePointFormat = models.CharField(max_length=256)
    suoAvailability = models.BooleanField()
    hasRamp = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    kep = models.FloatField()
    myBranch = models.FloatField()

    def __str__(self):
        return self.salePointName

