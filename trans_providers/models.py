# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as geomodels


class TransportProvider(models.Model):
    provider_id = models.UUIDField
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=16)
    lang = models.CharField(max_length=4)
    # https://github.com/django-money/django-money
    currency = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Transport Provider"
        verbose_name_plural = "TransportProviders "


class ServiceArea(models.Model):
    area_id = models.UUIDField
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    # https://docs.djangoproject.com/en/2.2/ref/contrib/gis/db-api/
    # https://docs.djangoproject.com/en/2.2/ref/contrib/gis/geos/
    area_polygon = geomodels.PolygonField()
    transport_provider = models.ForeignKey(
        TransportProvider, on_delete=models.CASCADE, related_name='service_areas')

    class Meta:
        verbose_name = "Service Area"
        verbose_name_plural = "Service Areas"
