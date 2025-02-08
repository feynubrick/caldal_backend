import pytest

from caldal.domain.schedule.services.logic.event_group_logic_service import (
    EventGroupLogicService,
)
from caldal.domain.schedule.models import EventGroup
from caldal.util.test.factories.account.user_factory import UserFactory
from caldal.util.test.factories.schedule.event_group_factory import EventGroupFactory


@pytest.mark.django_db
class TestEventGroupControllerBulkDelete:
    def test_one(self):
        user = UserFactory()
        event_group = EventGroupFactory(owner=user)

        assert EventGroup.objects.filter(uuid=event_group.uuid).exists()
        EventGroupLogicService().bulk_delete(user, [{"uuid": event_group.uuid}])
        assert not EventGroup.objects.filter(uuid=event_group.uuid).exists()

    def test_multiple(self):
        user = UserFactory()
        event_groups = [EventGroupFactory(owner=user) for _ in range(3)]
        uuids = [item.uuid for item in event_groups]
        assert EventGroup.objects.filter(uuid__in=uuids).count() == 3
        EventGroupLogicService().bulk_delete(user, [{"uuid": uuid} for uuid in uuids])
        assert EventGroup.objects.filter(uuid__in=uuids).count() == 0
