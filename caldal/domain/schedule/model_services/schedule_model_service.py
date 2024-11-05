from caldal.domain.schedule.models import Schedule
from caldal.util.services import ModelService


class ScheduleModelService(ModelService):
    _model = Schedule
