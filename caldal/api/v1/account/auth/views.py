from ninja import Router
from ninja_jwt.schema import TokenObtainPairOutputSchema, TokenRefreshInputSchema

from caldal.domain.account.const.enums import OAuthProviderEnum
from caldal.domain.account.services.logic import (
    CreateUserService,
    CreateUserServiceInputSchema,
)
from caldal.domain.account.services.model import UserModelService
from caldal.domain.common.auth.auth_token_service import AuthTokenService
from caldal.domain.common.auth.oauth_service import OAuthService

router = Router(tags=["auth"], auth=None)


@router.post(
    "/{provider}",
    response={(200, 201): TokenObtainPairOutputSchema},
)
def process_oauth(request, provider: OAuthProviderEnum, req_body):
    id_info = OAuthService(provider, req_body.platform).verify_token(req_body.token)
    identifier = id_info.sub
    email = id_info.email

    is_new_user = False
    if UserModelService().exists(
        oauth_profiles__provider=provider,
        oauth_profiles__identifier=identifier,
    ):
        user = UserModelService().get(
            oauth_profiles__provider=provider,
            oauth_profiles__identifier=identifier,
        )
    else:
        user = CreateUserService().run(
            CreateUserServiceInputSchema(
                email=email,
                provider=provider,
                identifier=identifier,
            )
        )
        is_new_user = True

    auth_service = AuthTokenService(user)
    refresh_token = auth_service.get_refresh_token()
    access_token = auth_service.get_access_token()

    status_code = 201 if is_new_user else 200

    return status_code, {
        "email": email,
        "refresh": refresh_token,
        "access": access_token,
    }


@router.post(
    "/refresh",
    response={200: TokenRefreshInputSchema.get_response_schema()},
)
def process_token(request, req_body: TokenRefreshInputSchema):
    return req_body.to_response_schema()
