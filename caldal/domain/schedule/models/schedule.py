from django.db import models
from django.utils.translation import gettext_lazy as _


class Schedule(models.Model):
    class Meta:
        db_table = "schedule_event"
        db_table_comment = "Schedules"
        app_label = "schedule"
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"
        ordering = ["id"]

    owner = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE,
        related_name="schedules",
        blank=False,
        null=False,
        verbose_name=_("Owner"),
        db_comment="Owner of the schedule",
        help_text=_("Owner of the schedule"),
    )
    content = models.TextField(
        null=True,
        blank=True,
        db_comment="스케쥴 내용",
        help_text=_("스케쥴 내용"),
    )
    date = models.DateField(
        null=False,
        blank=False,
        db_comment="스케쥴 날짜",
        help_text=_("스케쥴 날짜"),
        db_index=True,
    )
    start_time = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        db_comment="시작 시간",
        help_text=_("시작 시간"),
    )
    end_time = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        db_comment="시작 시간",
        help_text=_("시작 시간"),
    )
