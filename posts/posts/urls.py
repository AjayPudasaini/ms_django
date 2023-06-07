from django.contrib import admin
from django.urls import path
from posts.views import PostCreateApiView, PostListApiView, PostDetailAPIView, PostDeleteAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post-create', PostCreateApiView.as_view(), name="post_create"),
    path('api/posts', PostListApiView.as_view(), name="post_lists"),
    path('api/post/<int:pk>', PostDetailAPIView.as_view(), name="post_detail"),
    path('api/post-delete/<int:pk>', PostDeleteAPIView.as_view(), name="post_delete"),
]
