from django.urls import path
from .views import PostCreateView, PostDeleteView, PostRetrieveView, PostUpdateView

urlpatterns = [
    path('posts', PostCreateView.as_view(),name= 'create-post'),
    path('posts/<int:post_id>',PostRetrieveView.as_view(), name='retrieve-post'),
    path('posts/<int:post_id>/edit', PostUpdateView.as_view(), name='edit-post'),
    path('posts/<int:post_id>/delete', PostDeleteView.as_view(), name='delete-post'),
]