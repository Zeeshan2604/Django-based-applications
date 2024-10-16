from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('device/<int:device_id>/', views.device_detail, name='device_detail'),  # <int:device_id> captures an integer ID
    path('add_device/', views.add_device, name='add_device'),

]
