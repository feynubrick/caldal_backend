from django.db import models
from django.utils.translation import gettext_lazy as _

from caldal.domain.account.const.enums import OAuthProviderCodeEnum
from caldal.domain.account.const.values import (
    OAUTH_IDENTIFIER_MAX_LENGTH,
    OAUTH_PROVIDER_CODE_MAX_LENGTH,
)
from caldal.util.fields import CreatedAtField


class OAuthProfile(models.Model):
    class Meta:
        db_table = "account_oauth_profile"
        db_table_comment = "OAuth profile"
        app_label = "account"
        verbose_name = "OAuth Profile"
        verbose_name_plural = "OAuth Profiles"
        ordering = ["id"]
        unique_together = [["provider", "identifier"]]

    user = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE,
        related_name="oauth_profiles",
        db_comment="User profile",
        help_text=_("User profile"),
    )
    provider = models.CharField(
        max_length=OAUTH_PROVIDER_CODE_MAX_LENGTH,
        null=False,
        blank=False,
        choices=OAuthProviderCodeEnum.choices,
        db_comment="OAuth를 제공하는 플랫폼 이름: google, apple",
        help_text=_("OAuth를 제공하는 플랫폼 이름: google, apple"),
    )
    identifier = models.CharField(
        max_length=OAUTH_IDENTIFIER_MAX_LENGTH,
        null=False,
        blank=False,
        db_comment="플랫폼 내에서의 식별자",
        help_text=_("플랫폼 내에서의 식별자"),
    )
    created_at = CreatedAtField()
