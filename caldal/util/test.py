from datetime import datetime

from django.test import Client
from ninja_jwt.tokens import RefreshToken

from caldal.domain.account.models import User


def get_user_client(email: str) -> Client:
    user = User.objects.get(email=email)
    refresh_token = RefreshToken.for_user(user)
    return Client(HTTP_AUTHORIZATION=f"Bearer {refresh_token.access_token}")


def is_same_time(time1_str: str, time2_str: str) -> bool:
    time1 = datetime.fromisoformat(time1_str)
    time2 = datetime.fromisoformat(time2_str)
    return time1 == time2
