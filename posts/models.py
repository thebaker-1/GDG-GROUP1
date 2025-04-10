from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Post(models.Model):
    id = models.AutoField(primary_key=True) 
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)  
    content = models.TextField(null=False, blank=False)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  


    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"
