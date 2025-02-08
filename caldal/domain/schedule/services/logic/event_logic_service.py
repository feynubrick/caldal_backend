import copy
from typing import Any

from django.contrib.auth import get_user_model

from caldal.domain.schedule.services.model import EventGroupModelService
from caldal.domain.schedule.services.model.event_model_service import EventModelService
from caldal.domain.schedule.models import Event

User = get_user_model()


class EventLogicService:
    def bulk_create(
        self,
        requester: User,
        validated_data_list: list[dict[str, Any]],
    ):
        data_list = copy.deepcopy(validated_data_list)

        group_uuids = [data["group"]["uuid"] for data in data_list]
        group_maps = self._get_group_maps(requester, group_uuids)

        objs = []
        for data in data_list:
            group = group_maps[data.pop("group")["uuid"]]
            objs.append(Event(owner=requester, group=group, **data))
        EventModelService().bulk_create(objs)

    def bulk_update(
        self,
        requester: User,
        validated_data_list: list[dict[str, Any]],
    ):
        data_list = copy.deepcopy(validated_data_list)
        event_uuids = [data["uuid"] for data in data_list]
        qs = EventModelService().get_queryset()
        events = qs.filter(owner=requester, uuid__in=event_uuids)

        group_uuids = [data["group"]["uuid"] for data in data_list if "group" in data]
        group_uuids += [str(event.group.uuid) for event in events]
        group_maps = self._get_group_maps(requester, group_uuids)

        for data in data_list:
            if "group" in data:
                data["group"] = group_maps[data.pop("group")["uuid"]]
            qs.filter(owner=requester, uuid=data.pop("uuid")).update(**data)

    def bulk_delete(
        self,
        requester: User,
        validated_data_list: list[dict[str, Any]],
    ):
        EventModelService().get_queryset().filter(
            owner=requester,
            uuid__in=[data["uuid"] for data in validated_data_list],
        ).delete()

    def _get_group_maps(
        self,
        owner: User,
        uuids: list[str],
    ):
        groups = (
            EventGroupModelService().get_queryset().filter(owner=owner, uuid__in=uuids)
        )
        group_maps = {str(group.uuid): group for group in groups}
        return group_maps
