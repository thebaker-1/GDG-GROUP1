from django.urls import path
from .views import CommentPostView, FollowUserView, LikePostView, UnfollowUserView

urlpatterns = [
    path('posts/<int:post_id>/like', LikePostView.as_view(), name='like-post'),
    path('posts/<int:post_id>/comment', CommentPostView.as_view(), name='comment-post'),
    path('users/<int:user_id>/follow', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow', UnfollowUserView.as_view(), name='unfollow-user'),
]
