from django.contrib import admin
from django.urls import path
from django.conf import settings

from .api import api


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    path('backoffice/api/', api.urls)
]
