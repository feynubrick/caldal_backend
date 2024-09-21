from ninja import ModelSchema, Schema

from domain.account.models import User
from util.schemes import CamelCaseConfig


class UserOutSchema(ModelSchema):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
        ]

    class Config(CamelCaseConfig, Schema.Config):
        pass
