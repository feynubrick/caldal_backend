from ninja import Swagger
from ninja_extra import NinjaExtraAPI

from caldal.config.renderers import OrjsonRenderer
from caldal.domain.account.controllers import AuthController
from caldal.domain.schedule.controllers import (
    ScheduleController,
    ScheduleGroupController,
)

api = NinjaExtraAPI(
    renderer=OrjsonRenderer(),
    docs=Swagger(),
)

api.register_controllers(AuthController)
api.register_controllers(ScheduleController)
api.register_controllers(ScheduleGroupController)
