from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.BasicView.as_view()),
    path("auth/", include("rest_framework.urls")),
    path("create-user", views.CreateUserView.as_view()),
]
