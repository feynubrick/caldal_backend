from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedAtField(models.DateTimeField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("auto_now_add", True)
        kwargs.setdefault("null", False)
        kwargs.setdefault("blank", False)
        kwargs.setdefault("db_comment", "생성 시간")
        kwargs.setdefault("help_text", _("생성 시간"))
        super().__init__(*args, **kwargs)


class OrderIndexField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("db_index", True)
        kwargs.setdefault("null", False)
        kwargs.setdefault("blank", True)
        kwargs.setdefault("default", 0)
        super().__init__(*args, **kwargs)
