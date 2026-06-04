from django.conf import settings
from django.contrib import admin
from django.urls import path

from .api import api

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('backoffice/api/', api.urls),
]
