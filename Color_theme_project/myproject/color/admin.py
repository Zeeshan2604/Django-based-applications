from django.contrib import admin
from .models import Device
from django.utils.html import format_html


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

    search_fields = ('name', 'description')  

    class Media:
        css = {
            'all': ('color/css/admin_custom.css',) 
        }
        js = ('myapp/js/admin_custom.js',) 

def custom_index(request):
    devices_count = Device.objects.count()
    context = {
        'devices_count': devices_count,
    }
    return render(request, 'admin/index.html', context)

admin.site.index_template = 'admin/index.html'

class MyAdminSite(admin.AdminSite):
    site_header = "My Custom Admin"
    site_title = "Admin Panel"
    index_title = "Welcome to the Admin Panel"

    def each_context(self, request):
        context = super().each_context(request)
        context['admin_css'] = 'color/css/admin_custom.css' 
        context['admin_icon'] = 'https://example.com/favicon.ico'  
        return context

    



admin_site = MyAdminSite(name='myadmin')
admin.site = admin_site 
admin.site.site_header = "My Custom Admin Panel"
admin.site.site_title = "Admin Panel Title"
admin.site.index_title = "Welcome to My Admin Panel"    
admin.site.register(Device, DeviceAdmin)