"""
URL configuration for MatatuAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = 'Ma3 API',
        default_version = 'v1.0.0',
        description = 'Ma3 API more details to come later',
        terms_of_service = 'https://google.com/policies/terms',
        contact = openapi.Contact(email='githinjianthony720@gmail.com'), #email='ignatiusx47@gmail.com'),
        license = openapi.License(name='MIT License'),
    ),
    public = True,
    permission_classes = [permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-with-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-with-ui'),
    path('route/', include('route.urls'), name='route'),
    path('stop/', include('stop.urls'), name='stops'),
    path('fare/', include('fare.urls'), name='fare'),
    path('matatu/', include('matatu.urls'), name='matatuss'),
    path('bookings/', include('bookings.urls'), name='boookings')
]
