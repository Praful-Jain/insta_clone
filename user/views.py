from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View  # it directly renders our template
# from core.models import 


class ProfileView(View):
    template_name = 'user/profilepage.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
