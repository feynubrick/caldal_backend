from ninja import Schema


class ProcessOAuthInSchema(Schema):
    token: str


class IdTokenInfoSchema(Schema):
    sub: str
    email: str
