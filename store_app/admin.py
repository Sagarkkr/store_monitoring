from django.contrib import admin
from .models import Store, BusinessHour, StoreReport, StoreStatus

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_id','timezone_str']

@admin.register(BusinessHour)
class BusinessHourAdmin(admin.ModelAdmin):
    list_display = ['store', 'start_time_local', 'end_time_local']

@admin.register(StoreReport)
class StoreReportAdmin(admin.ModelAdmin):
    list_display = ['store', 'uptime_last_hour', 'downtime_last_hour']

admin.site.register(StoreStatus)
# class StoreStatusAdmin(admin.ModelAdmin):
#     list_display = []
