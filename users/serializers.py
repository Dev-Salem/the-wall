from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.conf import settings
from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "password", "profile_image", "email")


class CustomRegisterSerializer(RegisterSerializer):
    profile_image = serializers.ImageField(
        default="anon-profile.jpg",
        max_length=None,
        use_url=True,
        allow_null=True,
        required=False,
    )

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict["profile_image"] = self.validated_data.get("profile_image", "")
        return data_dict


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("profile_image",)
