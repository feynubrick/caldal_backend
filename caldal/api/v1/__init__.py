from ninja import NinjaAPI, Swagger
from ninja_jwt.authentication import JWTAuth

from caldal.api.v1.account import router as account_router
from caldal.api.v1.schedule import router as schedule_router
from caldal.config.renderers import OrjsonRenderer

api = NinjaAPI(
    docs=Swagger(),
    renderer=OrjsonRenderer(),
    auth=JWTAuth(),
)

api.add_router("/account", account_router)
api.add_router("/schedule", schedule_router)
