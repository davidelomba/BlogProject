from django.urls import path

from account.views import ShowProfilePage, EditProfilePage, CreateProfilePage
from . import views
from .views import PostDetail, UpdatePost, DeletePost, AddCategoryView, CategoryView, PostList, CategoryListView, \
    LikeView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post_detail/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add_post', views.add_post, name='add_post'),
    path('add_category', AddCategoryView.as_view(), name='add_category'),
    path('post_detail/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('post_detail/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('<int:pk>/profile/', ShowProfilePage.as_view(), name = 'profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePage.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePage.as_view(), name='create_profile_page'),
    path('post_detail/<int:pk>/add_comment', views.add_comment, name='add_comment'),
]
