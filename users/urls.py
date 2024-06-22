from django.urls import include, path

from . import views

urlpatterns = [
    path("auth-api/", include("rest_framework.urls")),
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
]
