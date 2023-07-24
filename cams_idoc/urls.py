# CAMS Asset Management System - CTCL 2017-2023
# Date: July 24, 2023 - July 24, 2023
# Purpose: Django views for the integrated documentation feature

urlpatterns = [
    path("docs/", docs_views.docs),
    path("docs/<str:page>/", docs_views.docs_page)
]