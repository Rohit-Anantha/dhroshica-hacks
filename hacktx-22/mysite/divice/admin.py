from django.contrib import admin

# Register your models here.

from .models import Image, Name, Item

admin.site.register(Image)
admin.site.register(Name)
admin.site.register(Item)