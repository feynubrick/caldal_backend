from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from caldal.domain.schedule.consts.values import EVENT_GROUP_NAME_MAX_LENGTH
from caldal.util.consts import COLOR_HEX_CODE_MAX_LENGTH
from caldal.util.fields import CreatedAtField, OrderIndexField, UpdatedAtField

UserModel = get_user_model()


class EventGroup(models.Model):
    class Meta:
        db_table = "schedule_event_group"
        db_table_comment = "이벤트 그룹"
        ordering = [
            "owner",
            "order_index",
        ]
        unique_together = [["owner", "uuid"]]

    uuid = models.UUIDField()
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="event_groups",
        blank=False,
        null=False,
        verbose_name=_("Owner"),
        db_comment="스케쥴 그룹 소유자",
        help_text=_("스케쥴 그룹 소유자"),
    )
    name = models.CharField(
        max_length=EVENT_GROUP_NAME_MAX_LENGTH,
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
    order_index = OrderIndexField(
        db_comment="순서를 정할 때 쓰는 값. 0이면 디폴트",
        help_text=_("순서를 정할 때 쓰는 값. 0이면 디폴트"),
    )
    created_at = CreatedAtField()
    updated_at = UpdatedAtField(auto_now=False)
