from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_image = models.ImageField(default="anon-profile.jpg", upload_to="profiles/")

    def __str__(self):
        return self.username
