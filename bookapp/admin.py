from django.contrib import admin

from . models import Category
from .models import data
from .models import ambulance_details

admin.site.register(Category)
admin.site.register(data)
admin.site.register(ambulance_details)

