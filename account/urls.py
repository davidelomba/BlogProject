from django.urls import path
from .views import UserRegistration, UserEdit, PasswordChange
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PasswordChange.as_view(template_name='registration/change_password.html'),
         name='change_password'),
    path('password_success/', views.password_success, name='password_success'),

]
