from trans_providers.models import TransportProvider, ServiceArea
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class TransportProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransportProvider
        fields = ['name', 'email', 'phone_no', 'lang', 'currency']


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    transport_provider = TransportProviderSerializer(read_only=True)

    class Meta:
        model = ServiceArea
        geo_field = "area_polygon"
        fields = ('id', 'name', 'transport_provider', 'price')
