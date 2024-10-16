from django.test import TestCase
from .models import Device

class DeviceModelTests(TestCase):
    def test_device_creation(self):
        device = Device.objects.create(
            name="Test Device",
            base_price=199.99,
            description="Test description",
            _stock=20,
            category="Test Category",
            manufacturer="Test Manufacturer"
        )
        self.assertEqual(device.name, "Test Device")
