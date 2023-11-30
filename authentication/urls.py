from django.urls import path
from authentication.views import SignUpView, LogInView

#  To pass a class based view in path use --> as_view() method with view name
urlpatterns = [
    path('', SignUpView.as_view(), name='signup_view'),
    path('login/', LogInView.as_view(), name ='login-view')
]