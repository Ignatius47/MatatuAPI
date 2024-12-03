from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Ma3 API',
        default_version='v1.0.0',
        description='Ma3 API for managing stops, routes, and fares. More details to come later.',
        terms_of_service='https://google.com/policies/terms',
        contact=openapi.Contact(email='ignatiusx47@gmail.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # API Schema Documentation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-with-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-with-ui'),

    # Matatu app
    path('matatu/', include('matatu.urls'), name='matatus'),

    # Uncomment these lines if you decide to use separate apps for routes, stops, and fares
    # path('route/', include('route.urls'), name='routes'),
    # path('stop/', include('stop.urls'), name='stops'),
    # path('fare/', include('fare.urls'), name='fares'),

    # Booking routes if applicable
    # path('bookings/', include('bookings.urls'), name='bookings'),
]