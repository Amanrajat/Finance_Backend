from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger config
schema_view = get_schema_view(
    openapi.Info(
        title="Finance Backend API",
        default_version='v1',
        description="Backend Developer Intern Assignment - Zorvyn",
        contact=openapi.Contact(email="aman@example.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # APIs
    path("api/", include([
        path("users/", include("apps.users.urls")),
        path("records/", include("apps.records.urls")),
        path("dashboard/", include("apps.dashboard.urls")),
    ])),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]