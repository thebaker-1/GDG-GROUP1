from django.shortcuts import render

# Create your views here .

from .models import Post
from .serializers import PostCreateSerializer, PostUpdateSerializer
from .serializers import PostRetrieveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PostCreateView(APIView):
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            post = serializer.save()
            return Response({ "id": post.id, "content": post.content, "created_at":post.created_at.isoformat()}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostRetrieveView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostRetrieveSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostUpdateView(APIView):
    def put(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id, user=request.user)
        except Post.DoesNotExist:
            return Response({"error": "Post not found or you do not have permission to edit this post."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostUpdateSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDeleteView(APIView):
    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id, user=request.user)
        except Post.DoesNotExist:
            return Response({"error": "Post not found or you do not have permission to delete this post."}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response({"message": "Post deleted successfully"}, status=status.HTTP_200_OK)
