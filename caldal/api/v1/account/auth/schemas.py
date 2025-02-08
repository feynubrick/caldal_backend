from ninja import Schema

from caldal.domain.account.const.enums import PlatformEnum


class ProcessOAuthInSchema(Schema):
    token: str
    platform: PlatformEnum
