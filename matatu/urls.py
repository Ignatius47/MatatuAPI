from django.urls import path, include
from rest_framework.routers import DefaultRouter
from routes.views.stop_views import StopViewSet
from routes.views.route_views import RouteViewSet

router = DefaultRouter()
router.register(r'stops', StopViewSet)
router.register(r'routes', RouteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]