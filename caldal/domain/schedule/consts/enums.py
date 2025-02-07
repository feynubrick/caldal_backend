from django.db.models import TextChoices


class EventTypeEnum(TextChoices):
    RANGED = "RANGED", "범위 이벤트"
    ALL_DAY = "ALL_DAY", "하루종일 이벤트"
