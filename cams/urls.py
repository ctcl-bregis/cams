from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("new/", views.new),
    path("view/<str:inid>/", views.view),
    path("edit/<str:inid>/", views.edit),
    path("delete/<str:inid>/", views.delete),
    path("settings/", views.settings),
    path("settings/exportcsv/", views.exportcsv),
    path("search/", views.search)
]
