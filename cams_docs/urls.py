# CAMS Asset Management System - CTCL 2017-2023
# File: urls.py
# Purpose: Integrated Documentation URLs
# Created: July 24, 2023
# Modified: July 25, 2023

from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.docs),
    path("<str:page>/", views.docs)
]