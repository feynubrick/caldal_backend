from ninja import Schema


class IdTokenInfoSchema(Schema):
    sub: str
    email: str
