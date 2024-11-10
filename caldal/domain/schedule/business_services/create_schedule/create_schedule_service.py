from caldal.util.services.business_service import BusinessService

from ...models import Schedule
from .create_schedule_service_input_schema import CreateScheduleServiceInputSchema


class CreateScheduleService(
    BusinessService[CreateScheduleServiceInputSchema, Schedule]
):
    def _run(self, data: CreateScheduleServiceInputSchema) -> Schedule:
        from caldal.domain.schedule.model_services import (
            ScheduleGroupModelService,
            ScheduleModelService,
        )

        if data.group_id is None:
            group = ScheduleGroupModelService().get_default(owner=data.owner)
        else:
            group = ScheduleGroupModelService().get(id=data.group_id)

        return ScheduleModelService().create(
            group=group,
            owner_id=data.owner,
            title=data.title,
            content=data.content,
            start_time=data.start_time,
            end_time=data.end_time,
            is_all_day=data.is_all_day,
        )
