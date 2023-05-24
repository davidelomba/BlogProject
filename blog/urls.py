from django.urls import path
from . import views
from .views import AddPost

urlpatterns = [
    path('', views.blog, name= 'home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('contact', views.contact, name='contact'),
    path('add_post', AddPost.as_view()),
]
