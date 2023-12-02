from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView  # it directly renders our template


class HomeView(TemplateView):
    template_name = 'core/feed.html'