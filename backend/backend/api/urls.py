from django.urls import path
from . import views

urlpatterns = [
    path("entries/", views.CreateEntry.as_view(), name="entry-list"),
    path("entries/delete/<int:pk>/", views.DeleteEntry.as_view(), name="delete-entry")
]
