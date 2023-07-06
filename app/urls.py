# CAMS - CTCL 2017-2023
# Date: July 5, 2023 - July 6, 2023
# Purpose: Django URL Configuration

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cams.urls"))
]