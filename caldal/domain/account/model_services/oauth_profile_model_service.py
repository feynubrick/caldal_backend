from caldal.domain.account.models import OAuthProfile
from caldal.util.services import ModelService


class OAuthProfileModelService(ModelService):
    _model = OAuthProfile
