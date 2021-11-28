from django.urls import path, include
from .views import HomeView, PostView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
  path('', HomeView.as_view(), name="home"),
  path('post/<int:pk>', PostView.as_view(), name="post_details"),
  path('post/<int:pk>/delete', DeletePostView.as_view(), name="post_delete"),
  path('post_create/', CreatePostView.as_view(), name="post_create"),
  path('post/update/<int:pk>', UpdatePostView.as_view(), name="post_update"),

]