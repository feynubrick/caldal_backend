import pytest


@pytest.fixture
def id_token_payload():
    # example ID Token's payload
    # https://developers.google.com/identity/openid-connect/openid-connect#an-id-tokens-payload
    return {
        "iss": "https://accounts.google.com",
        "azp": "1234987819200.apps.googleusercontent.com",
        "aud": "1234987819200.apps.googleusercontent.com",
        "sub": "10769150350006150715113082367",
        "at_hash": "HK6E_P6Dh8Y93mRNtsDB1Q",
        "hd": "example.com",
        "email": "jsmith@example.com",
        "email_verified": "true",
        "iat": 1353601026,
        "exp": 1353604926,
        "nonce": "0394852-3190485-2490358",
    }
