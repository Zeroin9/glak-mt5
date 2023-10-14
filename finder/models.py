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
    kep = models.BooleanField()
    myBranch = models.BooleanField()

    def __str__(self):
        return self.salePointName

class OfficeLoad(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    day = models.CharField(max_length=2)
    hour = models.CharField(max_length=5)
    percentage = models.IntegerField()