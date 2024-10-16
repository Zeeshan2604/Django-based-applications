from django.db import models
from model_utils.managers import InheritanceManager


class Device(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    _stock = models.PositiveIntegerField()  # Private attribute
    description = models.TextField()
    category = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)

    # Inheritance manager
    objects = InheritanceManager()

    def get_stock(self):
        return self._stock

    def set_stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative.")
        self._stock = value

    def __str__(self):
        return self.name

     # Default device type
    def get_device_type(self):
        return self.category
    
    def get_manf(self):
        return self.manufacturer


class Smartphone(Device):
    def get_device_type(self):
        return self.category
    
    def get_manf(self):
        return self.manufacturer



class Tablet(Device):
    def get_device_type(self):
        return self.category
    
    def get_manf(self):
        return self.manufacturer



class Laptop(Device):
    def get_device_type(self):
        return self.category
    
    def get_manf(self):
        return self.manufacturer

