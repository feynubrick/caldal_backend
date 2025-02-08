from ninja import Field, Schema
from pydantic import EmailStr

from caldal.domain.account.const.enums import OAuthProviderEnum
from caldal.domain.account.const.values import OAUTH_IDENTIFIER_MAX_LENGTH


class CreateUserServiceInputSchema(Schema):
    email: EmailStr
    provider: OAuthProviderEnum
    identifier: str = Field(max_length=OAUTH_IDENTIFIER_MAX_LENGTH)
