from django.urls import path
from . import views

urlpatterns = [
    path('entries/', views.list_entries, name='list_entries'),
    path('entry/create/', views.create_entry, name='create_entry'),
    path('entry/<int:pk>/', views.get_entry, name='get_entry'),
    path('entry/<int:pk>/update/', views.update_entry, name='update_entry'),
    path('entry/<int:pk>/delete/', views.delete_entry, name='delete_entry')
]
