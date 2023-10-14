from django.urls import path
from . import views

urlpatterns = [
    path('atms', views.atms_list, name='atms'),
    path('', views.office_list, name='offices'),
    # path('offices_add', views.office_add, name='bulk_offices'),
]