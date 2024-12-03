from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FareViewSet

router = DefaultRouter()
router.register(r'fares', FareViewSet)

urlpatterns = [
    path('fare/', include(router.urls)),
]