from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from caldal.domain.schedule.consts.enums import EventTypeEnum
from caldal.domain.schedule.consts.values import (
    EVENT_TITLE_MAX_LENGTH,
    EVENT_TYPE_MAX_LENGTH,
    TIMEZONE_MAX_LENGTH,
)
from caldal.util.fields import CreatedAtField, UpdatedAtField

UserModel = get_user_model()


class Event(models.Model):
    class Meta:
        db_table = "schedule_event"
        db_table_comment = "이벤트"
        ordering = [
            "owner",
            "type",
            "start_time",
        ]
        unique_together = [["owner", "uuid"]]

    uuid = models.UUIDField()
    type = models.CharField(
        max_length=EVENT_TYPE_MAX_LENGTH,
        choices=EventTypeEnum.choices,
        null=False,
        default=EventTypeEnum.RANGED,
        blank=False,
        db_comment="이벤트 유형: RANGED(범위), ALL_DAY(하루종일)",
        help_text=_("이벤트 유형: RANGED(범위), ALL_DAY(하루종일)"),
    )
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="events",
        blank=False,
        null=False,
        verbose_name=_("Owner"),
        db_comment="스케쥴 소유자",
        help_text=_("스케쥴 소유자"),
    )
    group = models.ForeignKey(
        "schedule.EventGroup",
        on_delete=models.PROTECT,
        related_name="events",
        blank=False,
        null=False,
        verbose_name=_("Group"),
        db_comment="스케쥴 그룹",
        help_text=_("스케쥴 그룹"),
    )
    title = models.CharField(
        max_length=EVENT_TITLE_MAX_LENGTH,
        null=False,
        blank=False,
        db_comment="스케쥴 제목",
        help_text=_("스케쥴 제목"),
    )
    content = models.TextField(
        null=True,
        blank=True,
        db_comment="스케쥴 내용",
        help_text=_("스케쥴 내용"),
    )
    start_time = models.DateTimeField(
        null=False,
        blank=False,
        db_index=True,
        db_comment="시작 시간",
        help_text=_("시작 시간"),
    )
    end_time = models.DateTimeField(
        null=False,
        blank=False,
        db_index=True,
        db_comment="종료 시간",
        help_text=_("종료 시간"),
    )
    timezone = models.CharField(
        max_length=TIMEZONE_MAX_LENGTH,
        default="Asia/Seoul",
        null=False,
        blank=True,
        db_comment="시간대. ex) Asia/Seoul",
        help_text=_("시간대. ex) Asia/Seoul"),
    )
    created_at = CreatedAtField()
    updated_at = UpdatedAtField(auto_now=False)
