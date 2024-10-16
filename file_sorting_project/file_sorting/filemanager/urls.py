from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('success/', views.success, name='success'),
    path('files/', views.file_list, name='file_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
