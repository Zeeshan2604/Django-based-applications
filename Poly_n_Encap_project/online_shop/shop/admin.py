from django.contrib import admin
from .models import Device, Laptop, Smartphone, Tablet  # Import your Device model

# Register the Device model
admin.site.register(Device)
admin.site.register(Smartphone)
admin.site.register(Tablet)
admin.site.register(Laptop)