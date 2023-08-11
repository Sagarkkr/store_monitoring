from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Store, BusinessHour, StoreStatus, StoreReport
from .serializers import StoreSerializer, BusinessHourSerializer, StoreStatusSerializers, StoreReportSerializer

class StoreViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class BusinessHourViewset(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin):
    
    queryset = BusinessHour.objects.all()
    serializer_class = BusinessHourSerializer

class StoreStatusViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin):
    
    queryset = StoreStatus.objects.all()
    serializer_class = StoreStatusSerializers

class StoreReportViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin):
    
    queryset = StoreReport.objects.all()