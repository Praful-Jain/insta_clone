from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from authentication.forms import UserForm, CustomUserChangeForm

User = get_user_model()

# Since we have altered the in-built 'User' model, made changes in it created a custom 'User' model and manager
# Now we have to create a custom model-admin
# Because if we use the default admin then their will be a security vulnerability because in it the admin can see the 'password' of the user
class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = User
    # for adding user .. fieldsets
    add_fieldsets = (
        ('Personal Details',{'fields':('email','full_name','username','picture', 'password1', 'password2')}),
        ('Permissions', {'fields':('is_staff','is_active')})
    )
    # for changing user fields .. fieldsets
    fieldsets = (
        ('Personal Details',{'fields':('email','full_name','username','picture')}),
        ('Permissions', {'fields':('is_staff','is_active')})
    )
    
admin.site.register(User, CustomUserAdmin)      # register our customUserAdmin