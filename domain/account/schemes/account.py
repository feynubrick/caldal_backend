from django.contrib.auth.models import User
from ninja import ModelSchema, Schema

from util.schemes import CamelCaseConfig


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
