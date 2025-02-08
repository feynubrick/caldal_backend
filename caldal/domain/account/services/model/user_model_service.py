from caldal.domain.account.models import User
from caldal.domain.common.services.model_service import ModelService


class UserModelService(ModelService):
    _model = User
