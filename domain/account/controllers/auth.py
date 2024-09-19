from ninja_extra import api_controller
from ninja_jwt.controller import NinjaJWTDefaultController


@api_controller(
    "account/auth/token",
    tags=["auth"],
    permissions=[],
)
class AuthController(NinjaJWTDefaultController):
    pass
