
from django.contrib import admin
from .models import CustomUser

# Register your models here.


class UserServiceAdmin(admin.ModelAdmin):
    list_display=['id','username','email','date_joined']
    list_display_links=['id','username','email']
    list_filter= []


admin.site.register(CustomUser,UserServiceAdmin)
