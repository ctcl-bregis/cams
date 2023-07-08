# CAMS Asset Management System - CTCL 2017-2023
# Date: June 9, 2023 (Reused from ContactList) - July 6, 2023
# Purpose: Main application URLs

from django.urls import path
from . import docs_views

urlpatterns = [
#    path("", views.index),
#    path("new/", views.new),
#    path("view/<str:inid>/", views.view),
#    path("edit/<str:inid>/", views.edit),
#    path("delete/<str:inid>/", views.delete),
#    path("settings/", views.settings),
#    path("settings/exportcsv/", views.exportcsv),
#    path("search/", views.search),
    path("docs/", docs_views.docs),
    path("docs/<str:page>/", docs_views.docs_page)
]
