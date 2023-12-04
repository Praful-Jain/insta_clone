from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View  # it directly renders our template
from core.forms import PostCreateForm
from core.models import Post

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
            return redirect('home_feed_view')       # if post saved successfully redirect to home_feed_view
        else:
            print(form.errors)
            print('invalid')
            return redirect('home_feed_view')
            return render(request, self.template_name, {'error':'Add image!'})   # otherwise render the error in the form
            