from rest_framework import serializers
from .models import Store, BusinessHour, StoreReport, StoreStatus

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'


class BusinessHourSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessHour
        fields = '__all__'

class StoreReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreReport
        fields = '__all__'

class StoreStatusSerializers(serializers.ModelSerializer):

    class Meta:
        model = StoreStatus
        fields = '__all__'