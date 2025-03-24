from django.contrib import admin
from .models import Log

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('phone', 'status', 'endpoint', 'created_at')
    search_fields = ('phone', 'endpoint', 'status')
    list_filter = ('status', 'created_at')
