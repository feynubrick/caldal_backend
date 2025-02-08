import pytest
from faker import Faker
from faker.providers import color

from caldal.domain.schedule.services.logic.event_group_logic_service import (
    EventGroupLogicService,
)
from caldal.domain.schedule.models import EventGroup
from caldal.util.test.factories.account.user_factory import UserFactory
from caldal.util.uuid import generate_uuid

fake = Faker()
fake.add_provider(color)


@pytest.mark.django_db
class TestEventGroupControllerBulkCreate:
    def test_create_one(self):
        user = UserFactory()
        data_list = [
            {
                "uuid": generate_uuid(),
                "name": fake.word()[:100],
                "color": fake.color(),
                "order_index": 0,
            }
        ]
        EventGroupLogicService().bulk_create(user, data_list)

        event_group = EventGroup.objects.first()
        assert str(event_group.uuid) == data_list[0]["uuid"]
        assert event_group.name == data_list[0]["name"]
        assert event_group.color == data_list[0]["color"]
        assert event_group.order_index == data_list[0]["order_index"]

    def test_create_multiple(self):
        user = UserFactory()
        data_list = [
            {
                "uuid": generate_uuid(),
                "name": fake.word()[:100],
                "color": fake.color(),
                "order_index": 0,
            },
            {
                "uuid": generate_uuid(),
                "name": fake.word()[:100],
                "color": fake.color(),
                "order_index": 1,
            },
        ]
        EventGroupLogicService().bulk_create(user, data_list)

        event_groups = EventGroup.objects.order_by("order_index")
        for event_group, data in zip(event_groups, data_list):
            assert str(event_group.uuid) == data["uuid"]
            assert event_group.name == data["name"]
            assert event_group.color == data["color"]
            assert event_group.order_index == data["order_index"]
