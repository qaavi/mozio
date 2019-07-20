# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
# from leaflet.admin import LeafletGeoAdmin
from .models import TransportProvider, ServiceArea


admin.site.site_header = "Mozio Admin"
admin.site.site_title = "Mozio"
admin.site.index_title = "Welcome to Mozio Portal"


@admin.register(TransportProvider)
class TransportProviderAdmin(OSMGeoAdmin):
    list_display = ('name', 'email', 'phone_no', 'lang', 'currency')
    # readonly_fields = ('status_time',)


@admin.register(ServiceArea)
class ServiceAreaAdmin(OSMGeoAdmin):
    list_display = ('name', 'price')

# admin.site.register(ServiceArea)
# admin.site.register(TransportProvider)
