from django.contrib import admin
from django.urls import path

from .api_v1 import api as api_v1
from .views import oauth_callback

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api_v1.urls),
    path("auth/<str:provider>/callback", oauth_callback, name="oauth_callback"),
]
