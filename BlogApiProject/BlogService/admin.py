from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import BlogPost,Category

# Register your models here.


class BlogServiceAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'publication_date']
    list_display_links=['id','title']
    list_filter= []

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id', 'name']
    list_display_links=['id','name']
    list_filter= []



admin.site.register(BlogPost,BlogServiceAdmin)
admin.site.register(Category,CategoryAdmin)



