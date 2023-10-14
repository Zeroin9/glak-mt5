from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#from .models import Office
from .models import OfficeLoad
# import json
import datetime
from . import sorter, dayhour

def office_list(request):
    offices_loads = {}
    is_search = False
    loads = OfficeLoad.objects.filter(date=datetime.date.today())

    offices = []
    for load in loads:
        office = load.office
        if office not in offices:
            offices.append(office)
        load_list = offices_loads.get(office, False)
        if not load_list:
            load_list = []
            offices_loads[office] = load_list
        load_list.append(load)

    if request.method == 'GET':
        filter_type = request.GET.get('filter_type', False)
        if not filter_type:
            pass
        else:
            is_search = True
            if filter_type == 'nearby':
                user_lon = request.GET.get('user_lon')
                user_lat = request.GET.get('user_lat')
                offices = sorter.sort_by_distance(offices, float(user_lon), float(user_lat))
            if filter_type == 'loadless':
                offices = sorter.sort_by_load(offices_loads, dayhour.get_current_day(), dayhour.get_current_hour())

    k=0
    offices_loads_list = []
    for office in offices:
        load_list = offices_loads.get(office, False)
        no_data = True
        if not load_list or len(load_list) < 1:
            no_data = False
        office_load = {'num': k, 'office': office, 'load_list': load_list}
        offices_loads_list.append(office_load)
        k += 1

    return render(request, 'finder/map.html', {'offices_loads_list': offices_loads_list, 'is_search': is_search})

# @csrf_exempt
# def office_add(request):
#     if request.method == 'POST':
#         offices_data_json = json.loads(request.body.decode('utf8'))
#         offices_data = offices_data_json['offices']
#         for data in offices_data:
#             office = Office(
#                 salePointName=data.get('salePointName'),
#                 address=data.get('address'),
#                 status=data.get('status'),
#                 rko=data.get('rko', False),
#                 officeType=data.get('officeType', False),
#                 officeTypeAdditional=data.get('officeTypeAdditional'),
#                 salePointFormat=data.get('salePointFormat'),
#                 suoAvailability=data.get('suoAvailability', False),
#                 hasRamp=data.get('hasRamp', False),
#                 latitude=data.get('latitude'),
#                 longitude=data.get('longitude'),
#                 kep=data.get('kep'),
#                 myBranch=data.get('myBranch', False)
#             )
#             office.save()
#         return JsonResponse({'ok': 'ok'})
#     else:
#         return JsonResponse({'error': 'DO POST'})

# @csrf_exempt
# def office_names(request):
#     offices_names = []
#     for office in Office.objects.all():
#         offices_names.append(office.salePointName)
#     return JsonResponse({"offices_names": offices_names})

# @csrf_exempt
# def load_add(request):
#     if request.method == 'POST':
#         loads_data_json = json.loads(request.body.decode('utf8'))
#         loads_data = loads_data_json['loads']
#         for data in loads_data:
#             office_name = data.get('office', False)
#             if not office_name:
#                 continue
#             office = Office.objects.get(salePointName=office_name)
#             if not office:
#                 continue
#             load = OfficeLoad(
#                 office=office,
#                 date=data.get('date'),
#                 day=data.get('day'),
#                 hour=data.get('hour'),
#                 percentage=data.get('load')
#             )
#             load.save()
#         return JsonResponse({'ok': 'ok'})
#     else:
#         return JsonResponse({'error': 'DO POST'})