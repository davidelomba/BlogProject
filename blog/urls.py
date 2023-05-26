from django.urls import path
from . import views
from .views import PostDetail, UpdatePost

urlpatterns = [
    path('', views.blog, name= 'home'),
    path('post_detail/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('contact', views.contact, name='contact'),
    path('add_post', views.add_post, name= 'add_post'),
    path('post_detail/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
]
