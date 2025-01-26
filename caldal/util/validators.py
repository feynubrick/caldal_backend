import re

from ninja import Field, Schema
from pydantic import field_validator


class ColorValidationMixin(Schema):
    color: str = Field(None, max_length=7)

    @field_validator("color")
    @classmethod
    def validate_color(cls, value: str):
        # 6자리 또는 3자리 헥스 컬러 코드 패턴
        pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

        if not re.match(pattern, value):
            raise ValueError("Invalid color code format. Must be #RRGGBB or #RGB")

        return value
