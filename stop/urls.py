from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StopViewSet

router = DefaultRouter()
router.register(r'', StopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
