from django.db.models import Max

from caldal.domain.account.models import User
from caldal.domain.schedule.consts.values import (
    DEFAULT_SCHEDULE_GROUP_COLOR_CODE,
    DEFAULT_SCHEDULE_GROUP_NAME,
)
from caldal.domain.schedule.models import ScheduleGroup
from caldal.util.services import ModelService


class ScheduleGroupModelService(ModelService):
    _model = ScheduleGroup

    def create_schedule_group(
        self,
        owner: User,
        name: str = DEFAULT_SCHEDULE_GROUP_NAME,
        color: str = DEFAULT_SCHEDULE_GROUP_COLOR_CODE,
        is_default: bool = False,
    ):
        if is_default:
            self.get_queryset().filter(owner=owner).update(is_default=False)
            order_index = 0
        else:
            max_order_index = (
                self.get_queryset()
                .filter(owner=owner)
                .aggregate(Max("order_index"))["order_index__max"]
            )
            order_index = max_order_index + 1

        return self.create(
            owner=owner,
            name=name,
            color=color,
            order_index=order_index,
            is_default=is_default,
        )

    def get_default(self, owner: User) -> ScheduleGroup:
        return self.get(owner=owner, is_default=True)
