import re


def is_valid_email(email: str) -> bool:
    # 기본적인 이메일 패턴
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return bool(re.match(pattern, email))