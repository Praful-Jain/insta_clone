from django.db import models
from django.contrib.auth import get_user_model
from core.utils import auto_save_current_user

User = get_user_model()

# Posts model
class Post(models.Model):
    text = models.CharField(max_length=140, blank=True, null=True)
    image = models.ImageField(upload_to='post_images')      # image stored in: root -> media -> post_images
    user = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)        # at the time of creating post we don't want to get asked for user, so we put its 'editable' attribute False
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # total_likes = models.IntegerField()
    # total_comments = models.IntegerField()
    def __str__(self):
        return str(self.pk)

    # to save the current loggedin user
    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Post, self).save(*args, **kwargs)

    # to get the number of likes on a post
    # reverse access --> from User to Post .... related_name='like_set' (by default)
    @property
    def likes_count(self):  
        count = self.like_set.count()
        return count

    @property
    def comments_count(self):  
        count = self.comment_set.count()
        return count

    # to get the number of users liked a particular post
    @property
    def liked_users(self):
        # Return the queryset of users who liked the post
        return User.objects.filter(like__post=self)

# Comments model
class Comment(models.Model):
    text = models.CharField(max_length=240)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Comment, self).save(*args, **kwargs)


# Likes model
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    liked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.post.id)

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Like, self).save(*args, **kwargs)


# Follows model
class Follow(models.Model):
    # reverse access --> from User to Follow .... related_name='follow_set' (by default)
    # In this model we will get error in reverse-access because in here we have declared 'User' as foreign key two times
    # To resolve this alter the related_name in relationships explicitly
    user = models.ForeignKey(User, related_name='follow_follower', on_delete=models.CASCADE, editable=False)
    followed = models.ForeignKey(User, related_name='follow_followed', on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} --> {self.followed}"
    
    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Follow, self).save(*args, **kwargs)