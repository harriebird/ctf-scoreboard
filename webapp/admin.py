from django.contrib import admin

from .models import Flag, Capture

# Register your models here.
class FlagAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'points']

admin.site.register(Flag, FlagAdmin)

class CaptureAdmin(admin.ModelAdmin):
    list_display = ['user', 'flag', 'time']

admin.site.register(Capture, CaptureAdmin)
