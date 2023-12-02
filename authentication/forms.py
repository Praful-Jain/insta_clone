from django import forms
from django.contrib.auth.forms import (UserCreationForm,      # Use this for password validation and matching, it has special fields 'password1' & 'password2'
    UserChangeForm)
# from user.models import User  -> we can also call it using
from django.contrib.auth import get_user_model   # it will fetch the user model     

class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'full_name', 'username', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'required': 'Compulsory'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

    # Adding placeholder to password1 and password2        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'   
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        
 
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'full_name', 'username']
