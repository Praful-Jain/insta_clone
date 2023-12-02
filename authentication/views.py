from django.shortcuts import render, redirect
from django.views.generic import View       # class based view(CBV)
from .forms import UserForm
from django.contrib.auth import (authenticate, login, logout, get_user_model)

User = get_user_model()

class SignUpView(View):
    template_name = 'authentication/signuppage.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:       
            return redirect('home_feed_view')
        fm = UserForm() 
        return render(request, self.template_name, {'form':fm})

    def post(self, request, *args, **kwargs):
        fm = UserForm(request.POST)         # create an instance of UserForm
        # breakpoint()
        if fm.is_valid():
            fm.save()       # save the user credientials into our database table User
            return redirect('login_view')        # if data is valid then redirect to next page ie.. login page
        else:       # if data not valid render the errors on webpage
            return render(request, self.template_name, {'form':fm})


        
class LogInView(View):
    template_name = 'authentication/loginpage.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:            # is user is already logged in, he will be redirected to home_feed
            return redirect('home_feed_view')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')
        
        try:
            user_obj = User.objects.get(username = email_username)      # get the user with this username
            email = user_obj.email      # find its email
        except Exception as e:
            email = email_username
            
        # if a user with these crediantials is present in our database then authenticate method 
        # will return the instance of that user
        user = authenticate(request, email = email, password = password)
        if user is None:    # is user not present in our database return to login page with the error
            return render(request, self.template_name, {'error':'Invalid login!'})   # we can also use messages in-built concept
        else:   # login the user
            login(request,user)
            return redirect('home_feed_view')        # redirect the user to its home page



class SignOutView(View):
    def post(self, request, *args, **kwargs):
        logout(request) # logout the user and redirect to login page         
        return redirect('login_view')
        