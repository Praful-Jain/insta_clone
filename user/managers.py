from django.contrib.auth.models import BaseUserManager

# Custom manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, username, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)     
        user_instance = self.model(email = email, username=username, **extra_fields)
        user_instance.set_password(password)
        user_instance.save()
        return user_instance

    def create_superuser(self, email, password, username, **extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, username, **extra_fields)
        