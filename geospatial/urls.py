from django.urls import path, include
from rest_framework.routers import  DefaultRouter
from geospatial.views import GeoSpatial

router=DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('geospatial/', GeoSpatial.as_view({'get': 'list'}), name='geospatial'),
    
]
