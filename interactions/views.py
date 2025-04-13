from django.shortcuts import render

# Create your views here.
from .models import Follow, Like
from .serializers import CommentCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from users.models import User

class LikePostView(APIView):
    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=request.user, post=post)
        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
    

class CommentPostView(APIView):
    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentCreateSerializer(data=request.data, context={'request': request, 'post': post})
        if serializer.is_valid():
            comment = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FollowUserView(APIView):
    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        if Follow.objects.filter(follower=request.user, following=user_to_follow).exists():
            return Response({"message": f"You are already following {user_to_follow.username}."}, status=status.HTTP_400_BAD_REQUEST)

        Follow.objects.create(follower=request.user, following=user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_201_CREATED)


class UnfollowUserView(APIView):
    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user == user_to_unfollow:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow_relationship = Follow.objects.filter(follower=request.user, following=user_to_unfollow).first()
        if not follow_relationship:
            return Response({"message": f"You are not following {user_to_unfollow.username}."}, status=status.HTTP_400_BAD_REQUEST)
        
        follow_relationship.delete()
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)