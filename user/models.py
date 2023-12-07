from django.db import models
from django.contrib.auth.models import AbstractUser     # AbstractBaseUser, AbstractUser, User
from user.managers import CustomUserManager                  # import custom manager

# Inherit 'AbstractUser' model's fields and add some new fields(ie.picture,full_name,email) and create a new model - custom User
class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 

    # optional fields
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phonenumber = models.CharField( max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    is_private_account = models.BooleanField(null=True, blank=True) 
    
    first_name = None   # no need of these pre-defined fields
    last_name = None  
        
    USERNAME_FIELD = 'email'              # 'email' field - used as a login credintial at the time of login (by default 'username' field is used)
    REQUIRED_FIELDS = ['full_name','username',]      # will pass those fields which we require (by default consider default fields)
    
    # Every Django model has at least one manager, and it's created by default if you don't explicitly define one.
    # A manager acts as a mediator between the database and the model,
    # Create a custom-manager explicitly and use it
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
        