from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import exceptions
from trans_providers.models import TransportProvider, ServiceArea
from . serializers import TransportProviderSerializer, ServiceAreaSerializer


class TransportProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TransportProvider.objects.all()
    serializer_class = TransportProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        queryset = ServiceArea.objects.all()
        lat = self.request.query_params.get('lat', None)
        lng = self.request.query_params.get('lng', None)
        if lat is not None and lng is not None:
            try:
                data_coordinates = [lat, lng]
                point = 'POINT(%s)' % ' '.join(map(str, data_coordinates))
            except (KeyError) as e:
                raise exceptions.ValidationError(
                    'Invalid lat/lng: %s' % e)
            queryset = queryset.filter(
                area_polygon__contains=point)
            return queryset
        return
