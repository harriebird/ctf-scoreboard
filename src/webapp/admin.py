from django.contrib import admin

from .models import Flag, Capture, Team, TeamMember

# Register your models here.
class FlagAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'points']

class CaptureAdmin(admin.ModelAdmin):
    list_display = ['user', 'flag', 'time']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Flag, FlagAdmin)
admin.site.register(Capture, CaptureAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMember)
