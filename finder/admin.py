from django.contrib import admin
from .models import ATM, Office, OfficeLoad

admin.site.register(ATM)
admin.site.register(Office)
admin.site.register(OfficeLoad)