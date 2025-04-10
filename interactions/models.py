from django.db import models

# Create your models here.
from django.db import models
from users.models import User  
from posts.models import Post  

class Comment(models.Model):
    id = models.AutoField(primary_key=True) 
    user = models.ForeignKey('users.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}"

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Like by {self.user.username} on Post {self.post.id}"

class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    follower = models.ForeignKey('users.User', related_name='following_set', on_delete=models.CASCADE)
    following = models.ForeignKey('users.User', related_name='followers_set', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"