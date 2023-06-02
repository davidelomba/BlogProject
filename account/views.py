from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from account.forms import SignUpForm, EditProfileForm, PasswordChangingForm


class UserRegistration(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEdit(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordChange(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})
