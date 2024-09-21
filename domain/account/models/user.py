from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
        db_comment="Email address",
        help_text=_("Email address"),
    )
