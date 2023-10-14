from django.urls import path
from . import views

urlpatterns = [
    path('atms', views.atms_list, name='atms'),
    path('', views.office_list, name='offices'),
    # path('offices_add', views.office_add, name='bulk_offices'),
    # path('office_names', views.office_names, name='office_names'),
    # path('load_add', views.load_add, name='bulk_officesload'),
]