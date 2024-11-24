import json

from django.http import HttpResponse
from ninja_extra import ControllerBase, api_controller, route
from ninja_jwt.schema import TokenObtainPairOutputSchema, TokenRefreshInputSchema

from caldal.domain.account.business_services import (
    AuthTokenService,
    CreateUserService,
    CreateUserServiceInputSchema,
    OAuthService,
)
from caldal.domain.account.const.enums import OAuthProviderEnum
from caldal.domain.account.model_services import UserModelService
from caldal.domain.account.models import User
from caldal.domain.account.schemas import ProcessOAuthInSchema


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

    @route.post(
        "/{provider}/callback",
        response={200: str},
    )
    def handle_oauth_redirect_uri(self, request, provider: OAuthProviderEnum):
        print(f"provider: {provider}")
        payload = json.loads(request.POST.get("payload", "{}"))
        print(f"payload: \n{json.dumps(payload, indent=4)}")
        html_response = """
            <html>
            <script>
                window.close();
            </script>
            </html>
            """
        return HttpResponse(content=html_response, media_type="text/html")

    @route.post(
        "/refresh",
        response={200: TokenRefreshInputSchema.get_response_schema()},
    )
    def refresh_token(self, request, req_body: TokenRefreshInputSchema):
        return req_body.to_response_schema()
