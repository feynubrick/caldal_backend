from caldal.domain.account.models import User
from caldal.domain.account.services.model import (
    OAuthProfileModelService,
    UserModelService,
)
from caldal.domain.common.service.logic_service import LogicService

from .create_user_logic_service_input_schema import CreateUserServiceInputSchema


class CreateUserService(LogicService[CreateUserServiceInputSchema, User]):
    def _before_run(self, data: CreateUserServiceInputSchema):
        pass

    def _run(self, data: CreateUserServiceInputSchema) -> User:
        user = UserModelService().create(
            username=data.email,
            email=data.email,
        )
        OAuthProfileModelService().create(
            user=user,
            provider=data.provider,
            identifier=data.identifier,
        )
        return user

    def _after_run(self, data: CreateUserServiceInputSchema, return_val: User):
        from caldal.domain.schedule.services.model import EventGroupModelService

        user = return_val
        EventGroupModelService().create(owner=user)
