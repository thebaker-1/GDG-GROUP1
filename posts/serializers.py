from rest_framework import serializers
from .models import Post
from interactions.models import Comment

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content']

    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(user=user, **validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'content']
        
    def create(self, validated_data):
        user = self.context['request'].user
        return Comment.objects.create(user=user, **validated_data)

class PostRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    likes = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'likes', 'comments']

    def get_likes(self, obj):
        return obj.likes.count()

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content', 'updated_at']
        read_only_fields = ['updated_at']
        