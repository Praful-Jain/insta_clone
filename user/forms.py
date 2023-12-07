from django import forms
from user.models import User

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['picture', 'full_name', 'username', 'email', 'bio', 'website', 'phonenumber', 'gender', 'is_private_account']
        
