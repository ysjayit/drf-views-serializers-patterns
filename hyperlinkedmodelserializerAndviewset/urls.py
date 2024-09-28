from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TypeViewSet, VehicleViewSet 


router = DefaultRouter()
router.register(r'types', TypeViewSet)
router.register(r'vehicles', VehicleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
