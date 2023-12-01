from django import forms
from django.contrib.auth.forms import UserCreationForm      # we can also use this for password validation and matching, it has special fields 'password1' & 'password2'
# from user.models import User  -> we can also call it using
from django.contrib.auth import get_user_model   # it will wetch the user model     

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
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        # Adding placeholder to password1
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        # Adding placeholder to password2
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        
    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     if len(password) < 8:  # Adjust the minimum length as needed
    #         raise forms.ValidationError("Invalid Password.")
    #     return password
