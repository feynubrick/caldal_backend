from caldal.util.schemas import CamelCaseSchema


class SignInGoogleInSchema(CamelCaseSchema):
    id_token: str


class AuthAccessTokenOutSchema(CamelCaseSchema):
    access_token: str


class AuthTokenOutSchema(AuthAccessTokenOutSchema):
    refresh_token: str


class RefreshTokenInSchema(CamelCaseSchema):
    refresh_token: str


class RefreshTokenOutSchema(AuthAccessTokenOutSchema):
    pass
