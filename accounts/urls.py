from django.urls import path
from .views import register  # Import the register view from accounts views

urlpatterns = [
    path('register/', register, name='register'),  # URL for registration
]