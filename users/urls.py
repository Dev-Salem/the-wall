from dj_rest_auth.registration.views import VerifyEmailView
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path("auth-api/", include("rest_framework.urls")),
    path("", include("dj_rest_auth.urls")),
    path("register/", views.CustomRegisterView.as_view()),
    re_path(
        r"^account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
]
