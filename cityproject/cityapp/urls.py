from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch-cities/', views.fetch_cities, name='fetch_cities'),
    path('get-states/', views.get_states, name='get_states'),  # For India states
]
