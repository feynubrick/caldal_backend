from caldal.domain.account.const.enums import OAuthProviderCodeEnum
from caldal.domain.account.services import UserModelService
from caldal.domain.account.services.model import OAuthProfileModelService


class UserLogicService:
    def create_user(self, email: str, provider: OAuthProviderCodeEnum, identifier: str):
        user = UserModelService().create(email=email)
        OAuthProfileModelService().create(
            user=user,
            provider=provider,
            identifier=identifier
        )
        return user