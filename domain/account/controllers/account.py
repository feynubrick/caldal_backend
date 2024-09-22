from django.contrib.auth import get_user_model
from ninja_extra import ControllerBase, api_controller, route
from ninja_jwt.tokens import RefreshToken

from domain.account.schemes import CreateAccountInSchema, CreateAccountOutSchema

User = get_user_model()


@api_controller(
    "account",
    tags=["account"],
    permissions=[],
)
class AccountController(ControllerBase):
    @route.post("/sign-up", response={201: CreateAccountOutSchema}, by_alias=True)
    def create_account(self, req_body: CreateAccountInSchema):
        data = req_body.dict()
        data["username"] = data["email"]
        user = User.objects.create_user(**data)
        refresh_token = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh_token),
            "access": str(refresh_token.access_token),
        }
