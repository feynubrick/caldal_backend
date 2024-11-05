from ninja_extra import ControllerBase, api_controller, route
from ninja_jwt.schema import TokenObtainPairOutputSchema, TokenRefreshInputSchema

from caldal.domain.account.business_services.auth_token_service import AuthTokenService
from caldal.domain.account.business_services.oauth_service import OAuthService
from caldal.domain.account.const.enums import OAuthProviderEnum
from caldal.domain.account.models import User
from caldal.domain.account.schemas import ProcessOAuthInSchema
from caldal.domain.schedule.business_services.create_user_service.create_user_service import (
    CreateUserService,
)
from caldal.domain.schedule.business_services.create_user_service.create_user_service_input_schema import (
    CreateUserServiceInputSchema,
)


@api_controller(
    "account/auth",
    tags=["auth"],
    permissions=[],
)
class AuthController(ControllerBase):
    @route.post(
        "/{provider}",
        response={(200, 201): TokenObtainPairOutputSchema},
    )
    def process_oauth(
        self,
        request,
        provider: OAuthProviderEnum,
        req_body: ProcessOAuthInSchema,
    ):
        id_info = OAuthService(provider).verify_token(req_body.id_token)
        identifier = id_info.sub
        email = id_info.email

        user_qs = User.objects.filter(
            oauth_profiles__provider=provider,
            oauth_profiles__identifier=identifier,
        )
        is_new_user = False
        if user_qs.exists():
            user = user_qs.get()
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

    @route.post(
        "/refresh",
        response={200: TokenRefreshInputSchema.get_response_schema()},
    )
    def refresh_token(self, request, req_body: TokenRefreshInputSchema):
        return req_body.to_response_schema()
