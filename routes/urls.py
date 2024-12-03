from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.stop_views import StopViewSet
from .views.route_views import RouteViewSet

router = DefaultRouter()
router.register(r'stops', StopViewSet)
router.register(r'routes', RouteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]