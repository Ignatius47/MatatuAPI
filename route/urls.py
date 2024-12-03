from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RouteViewSet

router = DefaultRouter()
router.register(r'route', RouteViewSet)

urlpatterns = [
    path('route/', include(router.urls)),
]