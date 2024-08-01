from django.contrib import admin

from main.models import Manufacture, Brand, Car, AdditionalCarImage

admin.site.register(AdditionalCarImage)
admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Manufacture)