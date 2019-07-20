from django.shortcuts import render
from rest_framework import viewsets
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
