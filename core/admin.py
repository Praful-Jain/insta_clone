from django.contrib import admin
from .models import Post, Comment, Like, Follow

# Creating custom model admins  (in order to see more fields)
class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('text','image','user','posted_on','updated_on')   # It is ModelAdmin's attribute --we will give the fields which we want to show to admin

class CommentModelAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('text', 'post', 'user', 'commented_on', 'updated_on')


class LikeModelAdmin(admin.ModelAdmin):
    model = Like
    list_display = ('post', 'user', 'liked_on', 'updated_on')


class FollowModelAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ('user', 'followed', 'followed_on', 'updated_on')


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Like, LikeModelAdmin)
admin.site.register(Follow, FollowModelAdmin)
