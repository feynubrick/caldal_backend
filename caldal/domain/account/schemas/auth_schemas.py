from ninja import Schema


class ProcessOAuthInSchema(Schema):
    id_token: str


class IdTokenInfoSchema(Schema):
    sub: str
    email: str
