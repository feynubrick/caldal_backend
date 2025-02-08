import jwt


def is_valid_jwt(token):
    jwt.decode(token, options={"verify_signature": False})
    return True