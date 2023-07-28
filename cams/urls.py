# CAMS Asset Management System - CTCL 2017-2023
# File: urls.py
# Purpose: Integrated Documentation URLs
# Created: July 26, 2023
# Modified: July 28, 2023

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index)
]
