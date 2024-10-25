from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "10.0.2.2",
    "14.40.31.174",
    "home.feynubrick.link",
]

NINJA_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

GOOGLE_OAUTH_REDIRECT_URI = "https://home.feynubrick.link/auth/google"
GOOGLE_OAUTH_CLIENT_ID = os.environ["GOOGLE_OAUTH_CLIENT_ID"]
