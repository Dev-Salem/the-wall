from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="The Wall API",
        default_version="v1",
        description="A simple social media app",
        terms_of_service="",
        contact=openapi.Contact(
            email="dev.salemsaleh@gmail.com",
        ),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("post/", include("post.urls")),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
