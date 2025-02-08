from caldal.domain.account.const.enums import OAuthProviderCodeEnum, PlatformEnum
from caldal.domain.external.apple.apple_oauth_provider import AppleOAuthProvider
from caldal.domain.external.google.google_oauth_provider import GoogleOAuthProvider

_provider_map = {
    OAuthProviderCodeEnum.GOOGLE: GoogleOAuthProvider,
    OAuthProviderCodeEnum.APPLE: AppleOAuthProvider,
}


class OAuthService:
    def __init__(self, provider_name: OAuthProviderCodeEnum, platform: PlatformEnum):
        self.platform = platform
        self.provider = self.get_provider(provider_name)

    def verify_token(self, token: str):
        return self.provider.verify_oauth_token(token)

    def get_provider(self, provider_name: OAuthProviderCodeEnum):
        return _provider_map[provider_name](self.platform)
