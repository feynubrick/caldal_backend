from caldal.domain.account.model_services import (
    OAuthProfileModelService,
    UserModelService,
)
from caldal.domain.account.models import User
from caldal.domain.schedule.business_services.create_user_service.create_user_service_input_schema import (
    CreateUserServiceInputSchema,
)
from caldal.util.services.business_service import BusinessService


class CreateUserService(BusinessService[CreateUserServiceInputSchema, User]):
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
        pass
