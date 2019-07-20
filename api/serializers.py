from trans_providers.models import TransportProvider, ServiceArea
from rest_framework import serializers


# HyperlinkedModelSerializer
class TransportProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportProvider
        fields = ['name', 'email', 'phone_no', 'lang', 'currency']


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'
