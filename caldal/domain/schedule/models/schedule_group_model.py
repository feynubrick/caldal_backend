from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from caldal.domain.schedule.consts.values import SCHEDULE_GROUP_NAME_MAX_LENGTH
from caldal.util.consts import COLOR_HEX_CODE_MAX_LENGTH
from caldal.util.fields import CreatedAtField, OrderIndexField


class ScheduleGroup(models.Model):
    class Meta:
        db_table = "schedule_group"
        db_table_comment = "스케쥴 그룹"
        app_label = "schedule"
        verbose_name = "ScheduleGroup"
        verbose_name_plural = "ScheduleGroups"
        ordering = [
            "owner",
            "order_index",
        ]

    owner = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE,
        related_name="schedule_groups",
        blank=False,
        null=False,
        verbose_name=_("Owner"),
        db_comment="스케쥴 그룹 소유자",
        help_text=_("스케쥴 그룹 소유자"),
    )
    name = models.CharField(
        max_length=SCHEDULE_GROUP_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        db_comment="스케쥴 그룹 이름",
        help_text=_("스케쥴 그룹 이름"),
    )
    color = models.CharField(
        max_length=COLOR_HEX_CODE_MAX_LENGTH,
        null=True,
        blank=True,
        db_comment="스케쥴 표시에 사용되는 색의 HEX 코드",
        help_text=_("스케쥴 표시에 사용되는 색의 HEX 코드"),
        validators=[
            RegexValidator(
                regex="^#([A-Fa-f0-9]{6})$",
                message="올바른 HEX 컬러 코드를 입력하세요",
            ),
        ],
    )
    is_default = models.BooleanField(
        default=False,
        null=False,
        blank=True,
        db_comment="디폴트 여부",
        help_text=_("디폴트 여부"),
    )
    order_index = OrderIndexField()
    created_at = CreatedAtField()
