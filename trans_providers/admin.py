# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import TransportProvider, ServiceArea


admin.site.site_header = "Mozio Admin"
admin.site.site_title = "Mozio"
admin.site.index_title = "Welcome to Mozio Portal"


@admin.register(TransportProvider)
class TransportProviderAdmin(OSMGeoAdmin):
    list_display = ('name', 'email', 'phone_no', 'lang', 'currency')


@admin.register(ServiceArea)
class ServiceAreaAdmin(OSMGeoAdmin):
    list_display = ('name', 'price', 'area_polygon')

# admin.site.register(ServiceArea)
