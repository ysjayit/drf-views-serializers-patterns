from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, PhoneViewSet


router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'phones', PhoneViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
