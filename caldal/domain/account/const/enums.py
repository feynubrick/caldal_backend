from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

class OAuthProviderEnum(TextChoices):
    GOOGLE = "GOOGLE", _("Google")
    APPLE = "APPLE", _("Apple")
