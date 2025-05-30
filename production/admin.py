from django.contrib import admin
from .models import WorkerProduction

@admin.register(WorkerProduction)
class WorkerProductionAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'machine_no', 'date', 'total_meter', 
        'avg_meter_per_day', 'rate_per_meter', 'total_rate'
    ]
    list_filter = ['date', 'machine_no', 'name']
    search_fields = ['name']
    readonly_fields = ['total_meter', 'total_rate', 'avg_meter_per_day', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'machine_no', 'date', 'rate_per_meter')
        }),
        ('Daily Meter Readings (Day 1-8)', {
            'fields': (
                'day_1_meter', 'day_2_meter', 'day_3_meter', 'day_4_meter',
                'day_5_meter', 'day_6_meter', 'day_7_meter', 'day_8_meter'
            )
        }),
        ('Daily Meter Readings (Day 9-15)', {
            'fields': (
                'day_9_meter', 'day_10_meter', 'day_11_meter', 'day_12_meter',
                'day_13_meter', 'day_14_meter', 'day_15_meter'
            )
        }),
        ('Calculated Fields', {
            'fields': ('total_meter', 'avg_meter_per_day', 'total_rate'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
