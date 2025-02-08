from caldal.domain.schedule.models import EventGroup
from caldal.domain.common.services.model_service import ModelService


class EventGroupModelService(ModelService):
    _model = EventGroup
