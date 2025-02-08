from caldal.domain.account.const.enums import OAuthProviderCodeEnum, PlatformEnum
from caldal.domain.account.services import UserModelService
from caldal.domain.account.services.logic.user_logic_service import UserLogicService
from caldal.domain.common.auth.auth_token_service import AuthTokenService
from caldal.domain.common.auth.oauth_service import OAuthService


class OAuthController:
    def __init__(
        self,
        provider: OAuthProviderCodeEnum,
        platform: PlatformEnum,
    ):
        self.provider = provider
        self.platform = platform
        self.oauth_service = OAuthService(provider, platform)

    def oauth_authenticate(self, token: str):
        id_info = self.oauth_service.verify_token(token)
        identifier = id_info.sub
        email = id_info.email

        is_created = False
        if UserModelService().exists(
            oauth_profiles__provider=self.provider,
            oauth_profiles__identifier=identifier,
        ):
            user = UserModelService().get(
                oauth_profiles__provider=self.provider,
                oauth_profiles__identifier=identifier,
            )
        else:
            user = UserLogicService().create_user(email, self.provider, identifier)
            is_created = True

        tokens = AuthTokenService(user).get_both_tokens()
        return is_created, user, tokens
