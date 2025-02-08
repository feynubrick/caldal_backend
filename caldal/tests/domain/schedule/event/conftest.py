import pytest
from faker import Faker

from caldal.domain.common.factories.account.user_factory import UserFactory
from caldal.domain.common.factories.schedule import EventGroupFactory

fake = Faker()


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def default_event_group(user):
    return EventGroupFactory(owner=user)
