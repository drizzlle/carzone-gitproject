from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style= "border-radius: 50px; "/>' .format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'
    list_display = ('id','thumbnail','car_title','city','model','year','body_style','fuel_type', 'is_featured')
    list_display_links = ('id','thumbnail','car_title')
    search_fields = ('id','car_title','city','model','year','fuel_type','body_style')
    list_filter = ('city','model','fuel_type','body_style')
    list_editable = ('is_featured',)
# Register your models here.

admin.site.register(Car, CarAdmin)
