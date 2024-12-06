from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import Matatu_Stages_viewsets


router = DefaultRouter()
router.register(r'', Matatu_Stages_viewsets)

urlpatterns = [
    path('', include(router.urls)),
]