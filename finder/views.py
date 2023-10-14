from django.shortcuts import render

def atms_list(request):
    return render(request, 'finder/map.html', {})