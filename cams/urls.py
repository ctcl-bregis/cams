# CAMS Asset Management System - CTCL 2017-2023
# Date: June 9, 2023 - July 24, 2023
# Purpose: Main application URLs

from django.urls import path

urlpatterns = [
    path("", views.index),
#    path("new/", views.new),
#    path("view/<str:inid>/", views.view),
#    path("edit/<str:inid>/", views.edit),
#    path("delete/<str:inid>/", views.delete),
#    path("settings/", views.settings),
#    path("settings/exportcsv/", views.exportcsv),
#    path("search/", views.search),
]
