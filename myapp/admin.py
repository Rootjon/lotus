from django.contrib import admin
from .models import Profile

# Register your models here.

class PrfileAdmin (admin. ModelAdmin):
    list_display =[
        'name',
        'age',
        'address',
        'image'
    ]
admin.site.register(Profile, PrfileAdmin)    