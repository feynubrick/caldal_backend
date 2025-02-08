from caldal.domain.account.models import User
from caldal.domain.common.service.model_service import ModelService


class UserModelService(ModelService):
    _model = User
