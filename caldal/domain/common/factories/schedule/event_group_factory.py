import factory
from faker import Faker
from faker.providers import color

from caldal.domain.schedule.models import EventGroup
from caldal.domain.common.factories.account.user_factory import UserFactory
from caldal.util.uuid import generate_uuid

fake = Faker()
fake.add_provider(color)


class EventGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EventGroup

    uuid = factory.LazyFunction(generate_uuid)
    owner = factory.SubFactory(UserFactory)
    name = factory.LazyFunction(fake.word)
    color = factory.LazyFunction(fake.color)
    order_index = factory.Sequence(lambda n: n)
