from django.conf import settings
from google.auth.transport import requests
from google.oauth2 import id_token
from ninja_extra import ControllerBase, api_controller, route
from ninja_jwt.schema import TokenObtainPairOutputSchema, TokenRefreshInputSchema
from ninja_jwt.tokens import RefreshToken

from caldal.domain.account.const.enums import OAuthProviderEnum
from caldal.domain.account.models import OAuthProfile, User
from caldal.domain.account.schemas import SignInGoogleInSchema


@api_controller(
    "account/auth",
    tags=["auth"],
    permissions=[],
)
class AuthController(ControllerBase):
    @route.post(
        "/google",
        by_alias=True,
        response={200: TokenObtainPairOutputSchema},
    )
    def process_google_oauth(self, request, req_body: SignInGoogleInSchema):
        id_info = id_token.verify_oauth2_token(
            id_token=req_body.id_token,
            request=requests.Request(),
            audience=settings.GOOGLE_OAUTH_CLIENT_ID,
        )

        identifier = id_info["sub"]
        email = id_info["email"]

        user_qs = User.objects.filter(
            oauth_profile__provider=OAuthProviderEnum.GOOGLE,
            oauth_profile__identifier=identifier,
        )
        if user_qs.exists():

            user = user_qs.get()
        else:
            user = User.objects.create_user(
                username=email,
                email=email,
            )
            OAuthProfile.objects.create(
                user=user,
                provider=OAuthProviderEnum.GOOGLE,
                identifier=identifier,
            )

        refresh_token = RefreshToken.for_user(user)
        return {
            "email": email,
            "refresh": str(refresh_token),
            "access": str(refresh_token.access_token),
        }

    @route.post(
        "/refresh",
        by_alias=True,
        response={200: TokenRefreshInputSchema.get_response_schema()},
    )
    def refresh_token(self, request, req_body: TokenRefreshInputSchema):
        return req_body.to_response_schema()
