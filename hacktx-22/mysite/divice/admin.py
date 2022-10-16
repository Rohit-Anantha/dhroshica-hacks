from django.contrib import admin

# Register your models here.

from .models import ImageItem, NameItem

admin.site.register(ImageItem)
admin.site.register(NameItem)