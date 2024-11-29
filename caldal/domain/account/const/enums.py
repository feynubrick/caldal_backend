from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class OAuthProviderEnum(TextChoices):
    GOOGLE = "google", _("Google")
    APPLE = "apple", _("Apple")


class PlatformEnum(TextChoices):
    IOS = "IOS", _("iOS")
    ANDROID = "ANDROID", _("Android")
