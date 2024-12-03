from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatatuViewSet

router = DefaultRouter()
router.register(r'matatu', MatatuViewSet)


urlpatterns = [
    path('', include(router.urls)),
]