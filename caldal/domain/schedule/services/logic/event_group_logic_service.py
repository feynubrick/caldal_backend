from typing import Any

from django.contrib.auth import get_user_model

from caldal.domain.schedule.services.model import EventGroupModelService
from caldal.domain.schedule.models import EventGroup

User = get_user_model()


class EventGroupLogicService:
    def bulk_create(
        self,
        requester: User,
        validated_data_list: list[dict[str, Any]],
    ):
        objs = [EventGroup(owner=requester, **data) for data in validated_data_list]
        EventGroupModelService().bulk_create(objs)

    def bulk_update(
        self,
        requester: User,
        validated_data_list: list[dict[str, Any]],
    ):
        qs = EventGroupModelService().get_queryset()
        for data in validated_data_list:
            uuid = data["uuid"]
            del data["uuid"]
            qs.filter(owner=requester, uuid=uuid).update(**data)

    def bulk_delete(
        self,
        requester: User,
        validated_data_list: list[dict[str, Any]],
    ):
        EventGroupModelService().get_queryset().filter(
            owner=requester,
            uuid__in=[data["uuid"] for data in validated_data_list],
        ).delete()
