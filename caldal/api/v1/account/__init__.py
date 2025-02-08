from ninja import Router
from caldal.api.v1.account.auth import router as auth_router

router = Router()

router.add_router("/auth", auth_router, auth=None)
