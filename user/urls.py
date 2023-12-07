from django.urls import path
from user.views import ProfileView, ProfileEditView
from django.contrib.auth.decorators import  login_required      # login decorator
# We want our home_feed to be accessible only when user is logged in

urlpatterns = [
    path('in/<str:username>/', login_required(ProfileView.as_view()) , name='profile_view'),
    path('in/<str:username>/edit/', login_required(ProfileEditView.as_view()), name='profile_edit_view'),
]