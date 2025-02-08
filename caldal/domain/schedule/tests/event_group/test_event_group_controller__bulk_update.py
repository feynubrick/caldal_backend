import pytest
from faker import Faker
from faker.providers import color

from caldal.domain.schedule.services.logic.event_group_logic_service import (
    EventGroupLogicService,
)
from caldal.util.test.factories.account.user_factory import UserFactory
from caldal.util.test.factories.schedule.event_group_factory import EventGroupFactory

fake = Faker()
fake.add_provider(color)


@pytest.mark.django_db
class TestEventGroupControllerBulkUpdate:
    def test_one(self):
        user = UserFactory()
        event_group = EventGroupFactory(owner=user)

        data_list = [
            {
                "uuid": event_group.uuid,
                "name": fake.word(),
                "color": fake.color(),
                "order_index": 1,
            }
        ]

        EventGroupLogicService().bulk_update(user, data_list)

        event_group.refresh_from_db()
        data = data_list[0]
        assert event_group.name == data["name"]
        assert event_group.color == data["color"]
        assert event_group.order_index == data["order_index"]

    def test_multiple(self):
        user = UserFactory()
        order_index_list = [0, 1, 2]
        event_groups = [EventGroupFactory(owner=user) for _ in order_index_list]

        data_list = [
            {
                "uuid": group.uuid,
                "name": fake.word(),
                "color": fake.color(),
                "order_index": order_index_list[i - 1]
            }
            for i, group in enumerate(event_groups)
        ]

        EventGroupLogicService().bulk_update(user, data_list)

        for event_group, data in zip(event_groups, data_list):
            event_group.refresh_from_db()
            assert event_group.name == data["name"]
            assert event_group.color == data["color"]
            assert event_group.order_index == data["order_index"]