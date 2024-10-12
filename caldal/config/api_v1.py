from ninja import Swagger
from ninja_extra import NinjaExtraAPI

from caldal.config.renderers import OrjsonRenderer
from caldal.domain.account.controllers import AccountController, AuthController
from caldal.domain.schedule.controllers import ScheduleController

api = NinjaExtraAPI(
    renderer=OrjsonRenderer(),
    docs=Swagger(),
)

api.register_controllers(AccountController)
api.register_controllers(AuthController)
api.register_controllers(ScheduleController)
