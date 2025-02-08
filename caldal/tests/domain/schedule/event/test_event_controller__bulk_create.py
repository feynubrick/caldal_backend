from datetime import datetime

import pytest
from faker import Faker

from caldal.domain.schedule.consts.enums import EventTypeEnum
from caldal.domain.schedule.services.logic.event_logic_service import EventLogicService
from caldal.domain.schedule.models import Event
from caldal.domain.common.factories.schedule import EventGroupFactory
from caldal.util.uuid import generate_uuid

fake = Faker()


@pytest.mark.django_db
class TestEventControllerBulkCreate:
    def test_one(self, user, default_event_group):
        """
        한 개의 이벤트를 생성
        """
        event_uuid = generate_uuid()
        data_list = [
            {
                "uuid": event_uuid,
                "type": EventTypeEnum.RANGED.value,
                "group": {"uuid": default_event_group.uuid},
                "title": fake.paragraph()[:200],
                "content": fake.paragraph(),
                "start_time": datetime.fromisoformat("2025-01-01T00:00:00+09:00"),
                "end_time": datetime.fromisoformat("2025-01-01T01:00:00+09:00"),
                "timezone": "Asia/Seoul",
            }
        ]
        EventLogicService().bulk_create(user, data_list)

        created_event = Event.objects.get(uuid=event_uuid)
        assert created_event.type == data_list[0]["type"]
        assert created_event.title == data_list[0]["title"]
        assert created_event.content == data_list[0]["content"]
        assert created_event.start_time == data_list[0]["start_time"]
        assert created_event.end_time == data_list[0]["end_time"]
        assert created_event.timezone == data_list[0]["timezone"]

    def test_multiple_in_the_same_group(self, user, default_event_group):
        """
        group이 같은 여러 개의 이벤트를 한번에 생성
        """
        data_list = [
            {
                "uuid": generate_uuid(),
                "type": EventTypeEnum.RANGED.value,
                "group": {"uuid": default_event_group.uuid},
                "title": fake.paragraph()[:200],
                "content": fake.paragraph(),
                "start_time": datetime.fromisoformat("2025-01-01T00:00:00+09:00"),
                "end_time": datetime.fromisoformat("2025-01-01T01:00:00+09:00"),
                "timezone": "Asia/Seoul",
            },
            {
                "uuid": generate_uuid(),
                "type": EventTypeEnum.RANGED.value,
                "group": {"uuid": default_event_group.uuid},
                "title": fake.paragraph()[:200],
                "content": fake.paragraph(),
                "start_time": datetime.fromisoformat("2025-01-02T00:00:00+09:00"),
                "end_time": datetime.fromisoformat("2025-01-02T01:00:00+09:00"),
                "timezone": "Asia/Seoul",
            },
        ]

        EventLogicService().bulk_create(user, data_list)
        for data in data_list:
            created_event = Event.objects.get(uuid=data["uuid"])
            assert created_event.type == data["type"]
            assert created_event.title == data["title"]
            assert created_event.content == data["content"]
            assert created_event.start_time == data["start_time"]
            assert created_event.end_time == data["end_time"]
            assert created_event.timezone == data["timezone"]
            assert created_event.group == default_event_group

    def test_multiple_with_different_groups(self, user, default_event_group):
        """
        group이 서로 다른 여러 개의 이벤트를 한번에 생성
        """
        second_event_group = EventGroupFactory(owner=user)
        data_list = [
            {
                "uuid": generate_uuid(),
                "type": EventTypeEnum.RANGED.value,
                "group": {"uuid": default_event_group.uuid},
                "title": fake.paragraph()[:200],
                "content": fake.paragraph(),
                "start_time": datetime.fromisoformat("2025-01-01T00:00:00+09:00"),
                "end_time": datetime.fromisoformat("2025-01-01T01:00:00+09:00"),
                "timezone": "Asia/Seoul",
            },
            {
                "uuid": generate_uuid(),
                "type": EventTypeEnum.RANGED.value,
                "group": {"uuid": second_event_group.uuid},
                "title": fake.paragraph()[:200],
                "content": fake.paragraph(),
                "start_time": datetime.fromisoformat("2025-01-02T00:00:00+09:00"),
                "end_time": datetime.fromisoformat("2025-01-02T01:00:00+09:00"),
                "timezone": "Asia/Seoul",
            },
        ]

        EventLogicService().bulk_create(user, data_list)
        for data, group in zip(data_list, [default_event_group, second_event_group]):
            created_event = Event.objects.get(uuid=data["uuid"])
            assert created_event.type == data["type"]
            assert created_event.title == data["title"]
            assert created_event.content == data["content"]
            assert created_event.start_time == data["start_time"]
            assert created_event.end_time == data["end_time"]
            assert created_event.timezone == data["timezone"]
            assert created_event.group == group
