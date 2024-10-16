from django.shortcuts import render, get_object_or_404
from .models import Device, Laptop, Smartphone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from model_utils.managers import InheritanceManager


def device_list(request):
    query = request.GET.get('search', '')  # Get search query from the URL
    if query:
        devices = Device.objects.filter(name__icontains=query)  # Filter by device name
    else:
        devices = Device.objects.all()  # Return all devices if no query


    return render(request, 'shop/device_list.html', {'devices': devices, 'query': query})


def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    stock = device.get_stock()
    device_type = device.get_device_type()

    return render(request, 'shop/device_detail.html', {
        'device': device,
        'stock': stock,
        'device_type': device_type

    })


@csrf_exempt
def add_device(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        base_price = request.POST.get('base_price')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        category = request.POST.get('category')
        manufacturer = request.POST.get('manufacturer')

        # Dynamically create the right subclass based on the category
        if category.lower() == 'smartphone':
            device = Smartphone(
                name=name,
                base_price=base_price,
                description=description,
                category=category,  # Directly use category from the POST data
                manufacturer=manufacturer  # Use manufacturer from POST data
            )
        elif category.lower() == 'laptop':
            device = Laptop(
                name=name,
                base_price=base_price,
                description=description,
                category=category,  # Directly use category from the POST data
                manufacturer=manufacturer  # Use manufacturer from POST data
            )
        else:
            device = Device(
                name=name,
                base_price=base_price,
                description=description,
                category=category,  # Directly use category from the POST data
                manufacturer=manufacturer  # Use manufacturer from POST data
            )

        # Set stock value after the device is created
        device.set_stock(int(stock))

        device.save()  # Save the device to the database
        return JsonResponse({'success': True, 'device_id': device.id})

    return JsonResponse({'success': False}, status=400)



