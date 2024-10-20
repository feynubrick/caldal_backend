from django.contrib.auth import get_user_model
from ninja import ModelSchema, Schema

from caldal.util.schemas import CamelCaseConfig

User = get_user_model()


class UserOutSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["email"]

    class Config(CamelCaseConfig, Schema.Config):
        pass
