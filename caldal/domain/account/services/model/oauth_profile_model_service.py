from caldal.domain.account.models import OAuthProfile
from caldal.domain.common.services.model_service import ModelService


class OAuthProfileModelService(ModelService):
    _model = OAuthProfile
