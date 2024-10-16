from django.urls import path
from . import views

urlpatterns = [
    path('', views.html_to_pdf, name='html_to_pdf'),
]
