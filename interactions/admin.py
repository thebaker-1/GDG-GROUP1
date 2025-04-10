from django.contrib import admin

# Register your models here.
from django.contrib import admin

from posts.models import Post
from .models import Comment, Like, Follow

# admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'created_at')
    fields = ('user', 'post', 'content')
    def save_model(self, request, obj, form, change):
        print(f"Saving comment: {obj}")
        print(f"User: {obj.user}, Post: {obj.post}")
        if not obj.user:
            obj.user = request.user  # Assign the currently logged-in admin user
        if not obj.post:
            obj.post = Post.objects.first()  # Assign the first post in the database
        super().save_model(request, obj, form, change)
