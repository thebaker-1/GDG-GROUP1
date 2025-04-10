from rest_framework import serializers
from .models import Comment

class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user  
        post = self.context['post']  
        return Comment.objects.create(user=user, post=post, **validated_data)