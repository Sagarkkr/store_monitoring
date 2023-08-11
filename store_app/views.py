from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Store, BusinessHour, StoreStatus, StoreReport
from .serializers import StoreSerializer, BusinessHourSerializer, StoreStatusSerializers, StoreReportSerializer

class StoreViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):
    """
        Store viewset to create a store and its timezone and list all stores
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class BusinessHourViewset(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin):
    """
        Business hour viewset to check business hour of all stores available
    """
    queryset = BusinessHour.objects.all()
    serializer_class = BusinessHourSerializer

class StoreStatusViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin):
    """
        Store status viewset for current status of stores
    """
    queryset = StoreStatus.objects.all()
    serializer_class = StoreStatusSerializers

class StoreReportViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin):
    """
        Store report viewset for reporting of all stores
    """
    queryset = StoreReport.objects.all()
    serializer_class = StoreReportSerializer
