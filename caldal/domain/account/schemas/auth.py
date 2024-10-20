from ninja import Schema

from caldal.util.schemes import CamelCaseConfig


class SignInGoogleInSchema(Schema):
    id_token: str

    class Config(CamelCaseConfig, Schema.Config):
        pass


class AuthTokenOutSchema(Schema):
    refresh_token: str
    access_token: str

    class Config(CamelCaseConfig, Schema.Config):
        pass
