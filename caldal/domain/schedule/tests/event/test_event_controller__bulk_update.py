from datetime import datetime
from zoneinfo import ZoneInfo
import pytest
from faker import Faker
from faker.providers import date_time

from caldal.domain.schedule.controllers.event_controller import EventController
from caldal.util.test.factories.schedule.event_factory import EventFactory
from caldal.util.test.factories.schedule.event_group_factory import EventGroupFactory

fake = Faker()
fake.add_provider(date_time)


@pytest.mark.django_db
class TestEventControllerBulkUpdate:
    def test_one(self, user, default_event_group):
        """
        한 개만 업데이트
        """
        event = EventFactory(owner=user, group=default_event_group)
        second_event_group = EventGroupFactory(owner=user)
        data_list = [
            {
                "uuid": event.uuid,
                "type": event.type,
                "group": {
                    "uuid": second_event_group.uuid,
                },
                "title": fake.sentence(),
                "content": fake.paragraph(),
                "start_time": datetime.fromisoformat("2025-01-01T00:00:00+09:00"),
                "end_time": datetime.fromisoformat("2025-01-01T01:00:00+09:00"),
                "timezone": "Asia/Seoul",
            },
        ]
        EventController().bulk_update(user, data_list)

        event.refresh_from_db()
        assert str(event.uuid) == str(data_list[0]["uuid"])
        assert event.type == data_list[0]["type"]
        assert str(event.group.uuid) == str(data_list[0]["group"]["uuid"])
        assert event.title == data_list[0]["title"]
        assert event.content == data_list[0]["content"]
        assert event.start_time == data_list[0]["start_time"]
        assert event.end_time == data_list[0]["end_time"]
        assert event.timezone == data_list[0]["timezone"]

    @pytest.mark.parametrize(
        "key, value",
        [
            ("title", fake.sentence()),
            ("content", fake.paragraph()),
            ("start_time", fake.date_time(tzinfo=ZoneInfo(fake.timezone()))),
            ("end_time", fake.date_time(tzinfo=ZoneInfo(fake.timezone()))),
            ("timezone", fake.timezone()),
            ("type", "RANGED"),
            ("type", "ALL_DAY"),
        ],
    )
    def test_partial_update_one_param_only__values(
        self, user, default_event_group, key, value
    ):
        """
        여러 개 업데이트: 같은 그룹
        """
        event = EventFactory(owner=user, group=default_event_group)
        data_list = [
            {
                "uuid": event.uuid,
                key: value,
            }
        ]
        EventController().bulk_update(user, data_list)

        event.refresh_from_db()
        data = data_list[0]
        assert getattr(event, key) == data[key]
