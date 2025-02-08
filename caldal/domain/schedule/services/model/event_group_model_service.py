from caldal.domain.schedule.models import EventGroup
from caldal.domain.common.service.model_service import ModelService


class EventGroupModelService(ModelService):
    _model = EventGroup
