from django.urls import path
from . import views

urlpatterns = [
    path('atms', views.atms_list, name='atms'),
]