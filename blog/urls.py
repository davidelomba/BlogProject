from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name= 'home'),
    path('contact', views.contact, name='contact'),
]
