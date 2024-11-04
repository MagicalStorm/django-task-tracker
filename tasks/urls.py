from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('edit/<int:pk>/', views.task_edit, name='task-edit'),
    path('delete/<int:pk>/', views.task_delete, name='task-delete'),
]