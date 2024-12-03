from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StopViewSet

router = DefaultRouter()
router.register(r'stop', StopViewSet)

urlpatterns = [
    path('stop/', include(router.urls)),
]
