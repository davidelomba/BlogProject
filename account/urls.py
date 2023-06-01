from django.urls import path
from .views import UserRegistration, UserEdit

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit_profile'),
]
