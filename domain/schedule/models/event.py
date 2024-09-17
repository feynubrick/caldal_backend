from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    class Meta:
        db_table = "schedule_event"
        db_table_comment = "Scheduled events"
        app_label = "schedule"
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["id"]

    title = models.CharField(
        max_length=255,
        db_comment="이벤트 제목",
        help_text=_("이벤트 제목"),
    )
    content = models.TextField(
        db_comment="이벤트 내용",
        help_text=_("이벤트 내용"),
    )
    is_all_day = models.DateField(
        null=False,
        blank=False,
        db_comment="하루 종일 지속되는 이벤트인지 나타내는 값",
        help_text=_("하루 종일 지속되는 이벤트인지 나타내는 값"),
    )
    start_time = models.DateTimeField(
        null=False,
        blank=True,
        db_comment="이벤트 시작 시간",
        help_text=_("이벤트 시작 시간"),
        db_index=True,
    )
    end_time = models.DateTimeField(
        null=True,
        blank=True,
        db_comment="이벤트 종료 시간. 하루종일 이벤트의 경우 null",
        help_text=_("이벤트 종료 시간. 하루종일 이벤트의 경우 null"),
    )
