from django.urls import path

from .views import UserAPIView, UserCreateAPIView, PostAPIView, PostCreateAPIView, CommentAPIView, \
    CommentCreateAPIView, LikeAPIView, LikeCreateAPIView

urlpatterns = [
    path('get/api/v1/users/', UserAPIView.as_view(), name='user-page'),
    path('post/api/v1/users/', UserCreateAPIView.as_view(), name='user-page'),
    path('get/api/v1/post/', PostAPIView.as_view(), name='post-page'),
    path('post/api/v1/post/', PostCreateAPIView.as_view(), name='post-page'),
    path('get/api/v1/comment/', CommentAPIView.as_view(), name='comment-page'),
    path('post/api/v1/comment/', CommentCreateAPIView.as_view(), name='comment-page'),
    path('get/api/v1/like/', LikeAPIView.as_view(), name='like-page'),
    path('post/api/v1/like/', LikeCreateAPIView.as_view(), name='like-page'),

]