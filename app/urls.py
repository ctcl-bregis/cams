# CAMS Asset Management System - CTCL 2017-2023
# File: urls.py
# Purpose: Main URLs configuration
# Created: July 22, 2023
# Modified: July 25, 2023

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/", include("cams.urls")),
    path("docs/", include("cams_docs.urls"))
]