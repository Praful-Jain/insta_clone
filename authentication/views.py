from django.shortcuts import render
from django.views.generic import View
from .forms import UserForm
from user.models import User

# Create your views here.
class SignUpView(View):
    template_name = 'authentication/signuppage.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        fm = UserForm(request.POST)         # create an instance of UserForm
        # breakpoint()
        if fm.is_valid():
            print('VALID')
        else:
            print('Invalid')
        return render(request, self.template_name)

    
class LogInView(View):
    template_name = 'authentication/loginpage.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass