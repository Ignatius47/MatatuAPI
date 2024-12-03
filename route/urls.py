from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RouteViewSet

router = DefaultRouter()
router.register(r'', RouteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]