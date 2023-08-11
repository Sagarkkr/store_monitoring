from rest_framework import routers
from .views import StoreViewSet, BusinessHourViewset, StoreStatusViewSet, StoreReportViewSet

store_routers = routers.DefaultRouter()
store_routers.register('store', StoreViewSet, basename='store')
store_routers.register('business_hour', BusinessHourViewset, basename='business_hour')
store_routers.register('store_status', StoreStatusViewSet, basename='store_status')
store_routers.register('store_report', StoreReportViewSet, basename='store_report')