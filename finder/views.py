from django.shortcuts import render
#from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from .models import ATM
from .models import Office
#import json

def atms_list(request):
    return render(request, 'finder/map.html', {'atms': ATM.objects.all()})

def office_list(request):
    return render(request, 'finder/map.html', {'offices': Office.objects.all()})

# @csrf_exempt
# def office_add(request):
#     if request.method == 'POST':
#         offices_data_json = json.loads(request.body.decode('utf8'))
#         offices_data = offices_data_json['offices']
#         for data in offices_data:
#             # Create an instance of the Office model using the deserialized data
#             office = Office(
#                 salePointName=data['salePointName'],
#                 address=data['address'],
#                 status=data['status'],
#                 rko=data['rko'],
#                 officeType=data['officeType'],
#                 officeTypeAdditional=data['officeTypeAdditional'],
#                 salePointFormat=data['salePointFormat'],
#                 suoAvailability=data['suoAvailability'],
#                 hasRamp=data['hasRamp'],
#                 latitude=data['latitude'],
#                 longitude=data['longitude'],
#                 kep=data['kep'],
#                 myBranch=data['myBranch']
#             )
#             # Save the instance to persist the data in the database
#             office.save()
#         return JsonResponse({'ok': 'ok'})
#     else:
#         return JsonResponse({'error': 'DO POST'})