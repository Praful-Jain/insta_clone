from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View  # it directly renders our template
from user.models import User
from core.models import Follow
from user.forms import UserProfileEditForm


class ProfileView(View):
    authenticated_template = 'user/authenticated_profilepage.html'
    anonymous_template = 'user/anonymous_profilepage.html'
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        try:
            obj = User.objects.get(username = username)
        except:
            return HttpResponse('<h1>This page does not exist.</h1>')

        if username == request.user.username:   # Logged in user visiting it's own profile
            return render(request, self.authenticated_template, {'user':obj})
        else:       # Logged in user visiting other user's profile
            return render(request, self.anonymous_template, {'user':obj})
     
        
class ProfileEditView(View):
    authenticated_template = 'user/authenticated_profilepage.html'
    template_name = 'user/profile_edit.html'
    def get(self,request, *args, **kwargs):
        form = UserProfileEditForm(instance=request.user)
        return render(request, self.template_name, {'form':form})
    
    def post(self,request, *args, **kwargs):
        form = UserProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            print('success')
            return redirect('profile_view', username=form.cleaned_data['username'])
        else:
            print('failure')
            print(form.errors)
            return render(request, self.template_name, {'form':form})   # otherwise render the error in the form
