from caldal.domain.account.models import User
from caldal.util.services import ModelService


class UserModelService(ModelService):
    _model = User
