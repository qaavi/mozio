from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'trans_providers', views.TransportProviderViewSet)
router.register(r'service_areas', views.ServiceAreaViewSet)

schema_view = get_swagger_view(title='Mozio API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view)
]
