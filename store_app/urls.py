from rest_framework import routers
from .views import StoreViewSet

store_routers = routers.DefaultRouter()
store_routers.register('store', StoreViewSet, basename='store')