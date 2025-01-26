from django.contrib import admin
from django.urls import path

from .views import oauth_callback

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/<str:provider>/callback", oauth_callback, name="oauth_callback"),
]
