from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ATM
from .models import Office
import json

def atms_list(request):
    return render(request, 'finder/map.html', {'atms': ATM.objects.all()})

def office_list(request):
    return render(request, 'finder/map.html', {'offices': Office.objects.all()})

@csrf_exempt
def office_add(request):
    if request.method == 'POST':
        offices_data_json = json.loads(request.body.decode('utf8'))
        offices_data = offices_data_json['offices']
        for data in offices_data:
            # Create an instance of the Office model using the deserialized data
            office = Office(
                salePointName=data.get('salePointName'),
                address=data.get('address'),
                status=data.get('status'),
                rko=data.get('rko', False),
                officeType=data.get('officeType', False),
                officeTypeAdditional=data.get('officeTypeAdditional'),
                salePointFormat=data.get('salePointFormat'),
                suoAvailability=data.get('suoAvailability', False),
                hasRamp=data.get('hasRamp', False),
                latitude=data.get('latitude'),
                longitude=data.get('longitude'),
                kep=data.get('kep'),
                myBranch=data.get('myBranch', False)
            )
            # Save the instance to persist the data in the database
            office.save()
        return JsonResponse({'ok': 'ok'})
    else:
        return JsonResponse({'error': 'DO POST'})