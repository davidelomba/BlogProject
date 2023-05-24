from django.urls import path
from . import views
from .views import AddPost, PostDetail

urlpatterns = [
    path('', views.blog, name= 'home'),
    path('post_detail/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('contact', views.contact, name='contact'),
    path('add_post', AddPost.as_view(), name= 'add_post'),
]
