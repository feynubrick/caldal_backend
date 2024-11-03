from caldal.domain.account.const.enums import OAuthProviderEnum
from caldal.domain.external.google.oauth_provider import GoogleSocialOAuthProvider

_provider_map = {OAuthProviderEnum.GOOGLE: GoogleSocialOAuthProvider}


class OAuthService:
    def __init__(self, provider_name: str):
        self.provider = self.get_provider(provider_name)

    def verify_token(self, token: str):
        return self.provider.verify_oauth_token(token)

    def get_provider(self, provider_name: str):
        return _provider_map[self._get_provider_name(provider_name)]()

    def _get_provider_name(self, value: str) -> OAuthProviderEnum:
        return OAuthProviderEnum(value.upper())
