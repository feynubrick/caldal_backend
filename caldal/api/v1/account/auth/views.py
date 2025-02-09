from ninja import Router
from ninja_jwt.schema import TokenObtainPairOutputSchema, TokenRefreshInputSchema

from caldal.api.v1.account.auth.schemas import ProcessOAuthInSchema
from caldal.domain.account.const.enums import OAuthProviderCodeEnum
from caldal.domain.account.controllers.auth.oauth_controller import OAuthController

router = Router(tags=["auth"])


@router.post(
    "/refresh",
    response={200: TokenRefreshInputSchema.get_response_schema()},
    auth=None,
)
def refresh_token(request, req_body: TokenRefreshInputSchema):
    return req_body.to_response_schema()


@router.post(
    "/{provider}",
    response={(200, 201): TokenObtainPairOutputSchema},
    auth=None,
)
def oauth_authenticate(
    request,
    provider: OAuthProviderCodeEnum,
    payload: ProcessOAuthInSchema,
):
    is_new_user, user, tokens = OAuthController(
        provider,
        platform=payload.platform,
    ).oauth_authenticate(token=payload.token)
    status_code = 201 if is_new_user else 200

    return status_code, {
        "email": user.email,
        "access": str(tokens["access"]),
        "refresh": str(tokens["refresh"]),
    }
