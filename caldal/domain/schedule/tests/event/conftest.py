import pytest
from faker import Faker

from caldal.util.test.factories.account.user_factory import UserFactory
from caldal.util.test.factories.schedule.event_group_factory import EventGroupFactory

fake = Faker()


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def default_event_group(user):
    return EventGroupFactory(owner=user)
