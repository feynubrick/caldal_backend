from django.db import models
from django.utils.translation import gettext_lazy as _

from caldal.domain.schedule.consts.values import (
    DEFAULT_TIMEZONE,
    SCHEDULE_TIMEZONE_MAX_LENGTH,
    SCHEDULE_TITLE_MAX_LENGTH,
)
from caldal.util.fields import CreatedAtField


class Schedule(models.Model):
    class Meta:
        db_table = "schedule_schedule"
        db_table_comment = "Schedules"
        app_label = "schedule"
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"
        ordering = ["owner", "start_time"]

    owner = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE,
        related_name="schedules",
        blank=False,
        null=False,
        verbose_name=_("Owner"),
        db_comment="스케쥴 소유자",
        help_text=_("스케쥴 소유자"),
    )
    group = models.ForeignKey(
        "schedule.ScheduleGroup",
        on_delete=models.PROTECT,
        related_name="schedules",
        blank=False,
        null=False,
        verbose_name=_("Group"),
        db_comment="스케쥴 그룹",
        help_text=_("스케쥴 그룹"),
    )
    title = models.CharField(
        max_length=SCHEDULE_TITLE_MAX_LENGTH,
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
    is_all_day = models.BooleanField(
        null=False,
        default=False,
        blank=False,
        db_comment="종일 이벤트인지 나타내는 값",
        help_text=_("종일 이벤트인지 나타내는 값"),
    )
    timezone = models.CharField(
        max_length=SCHEDULE_TIMEZONE_MAX_LENGTH,
        null=False,
        blank=False,
        default=DEFAULT_TIMEZONE,
        db_comment="시간대. ex) Asia/Seoul",
        help_text=_("시간대. ex) Asia/Seoul"),
    )
    created_at = CreatedAtField()
