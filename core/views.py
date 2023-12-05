from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View  # it directly renders our template
from core.forms import PostCreateForm
from core.models import Post, Like, Comment

class HomeView(View):
    template_name = 'core/base.html'
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        all_posts = Post.objects.all().order_by('-posted_on')
        return render(request, self.template_name, {'form':form, 'all_posts':all_posts})
    
    
class PostCreateView(View):
    template_name = 'core/base.html'
    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            print('success')
            form.save()     # save the user's post in 'Post' table
            return redirect(request.META.get('HTTP_REFERER'))
            return redirect('home_feed_view')       # if post saved successfully redirect to home_feed_view
        else:
            print(form.errors)
            print('invalid')
            return redirect(request.META.get('HTTP_REFERER'))
            return redirect('home_feed_view')
            return render(request, self.template_name, {'error':'Add image!'})   # otherwise render the error in the form
           
           
class PostLikeUnlikeView(View):
    template_name = 'core/base.html'
    def post(self, request, *args, id):
        post_id = id 
        try:    # If the user already liked that post: unlike it.. delete the entry in the Likes model            
            like_object = Like.objects.get(user = request.user, post_id = post_id)
            like_object.delete()
        except Exception as e:  # otherwise: lite it ... create an entry in the Likes model
            Like.objects.create(user = request.user, post_id = post_id)  # django will handle it
        return redirect(request.META.get('HTTP_REFERER'))


class PostCommentView(View):
    template_name = 'core/base.html'
    def post(self, request, *args, id):
        post_id = id 
        # "request.POST" contains information of all the fields which are submitted
        # So we can fetch a particular field by it's name attribute
        comment_text = request.POST.get('comment_text')
        if len(comment_text) != 0:
            Comment.objects.create(post_id=post_id, text=comment_text)
        print(request.user.username)
        return redirect(request.META.get('HTTP_REFERER'))

class CommentsView(View):
    def get(self, request, *args, id):
        post_id = id
        post = Post.objects.get(pk=post_id)
        return render(request, 'core/popup_comment.html', {'post':post})
    