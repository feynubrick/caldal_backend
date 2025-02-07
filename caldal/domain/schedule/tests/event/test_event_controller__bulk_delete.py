import pytest
from faker import Faker

from caldal.domain.schedule.controllers.event_controller import EventController
from caldal.domain.schedule.models import Event
from caldal.util.test.factories.schedule.event_factory import EventFactory

fake = Faker()


@pytest.mark.django_db
class TestEventControllerBulkUpdate:
    def test_one(self, user, default_event_group):
        """
        한 개만 삭제
        """
        event = EventFactory(owner=user, group=default_event_group)
        data_list = [{"uuid": event.uuid}]
        EventController().bulk_delete(user, data_list)

        assert not Event.objects.filter(id=event.id).exists()

    def test_one_in_multiple(self, user, default_event_group):
        """
        여러 개 중 하나 삭제
        """

        events = [
            EventFactory(owner=user, group=default_event_group),
            EventFactory(owner=user, group=default_event_group),
        ]
        data_list = [{"uuid": events[0].uuid}]
        EventController().bulk_delete(user, data_list)

        assert not Event.objects.filter(id=events[0].id).exists()
        assert Event.objects.filter(id=events[1].id).exists()