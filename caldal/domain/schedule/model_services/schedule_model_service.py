from caldal.domain.account.models import User
from caldal.domain.schedule.models import Schedule
from caldal.util.services import ModelService


class ScheduleModelService(ModelService):
    _model = Schedule

    def get_list_of_schedule(self, owner: User):
        return (
            self.get_queryset()
            .filter(owner=owner)
            .order_by("start_time")
            .prefetch_related("group")
        )
