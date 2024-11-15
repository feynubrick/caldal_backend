from ninja import ModelSchema

from caldal.domain.schedule.models import Schedule


class CreateScheduleServiceInputSchema(ModelSchema):
    group_id: int | None = None

    class Meta:
        model = Schedule
        fields = [
            "owner",
            "title",
            "content",
            "start_time",
            "end_time",
            "is_all_day",
            "timezone",
        ]
