from datetime import timedelta

import factory
from django.utils import timezone
from faker import Faker
from faker.providers import color

from caldal.domain.schedule.consts.enums import EventTypeEnum
from caldal.domain.schedule.models import Event
from caldal.domain.common.factories.account.user_factory import UserFactory
from caldal.domain.common.factories.schedule.event_group_factory import EventGroupFactory
from caldal.util.uuid import generate_uuid

fake = Faker()
fake.add_provider(color)


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    uuid = factory.LazyFunction(generate_uuid)
    type = EventTypeEnum.RANGED
    owner = factory.SubFactory(UserFactory)
    group = factory.SubFactory(EventGroupFactory)
    title = factory.LazyFunction(fake.sentence)
    content = factory.LazyFunction(fake.paragraph)
    start_time = factory.LazyFunction(timezone.now)
    end_time = factory.LazyAttribute(lambda obj: obj.start_time + timedelta(hours=1))
    timezone = "Asia/Seoul"
