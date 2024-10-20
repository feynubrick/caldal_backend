from caldal.util.schemas import CamelCaseSchema


class SignInGoogleInSchema(CamelCaseSchema):
    id_token: str
