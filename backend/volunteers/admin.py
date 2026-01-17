from django.contrib import admin
from .models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'skills', 'hours_per_week', 'created_at')
    list_filter = ('skills', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)