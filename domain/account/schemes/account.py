from django.contrib.auth import get_user_model
from ninja import ModelSchema, Schema

from util.schemes import CamelCaseConfig

User = get_user_model()


class CreateAccountInSchema(ModelSchema):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]

    class Config(CamelCaseConfig, ModelSchema.Config):
        pass


class CreateAccountOutSchema(Schema):
    access: str
    refresh: str

    class Config(CamelCaseConfig, Schema.Config):
        pass
