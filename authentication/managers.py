from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password



class UserManager(BaseUserManager):
    """
    ~custom user model manager.
    """   
    def create_user(self, phone_number, password, **extra_fields):
        if phone_number is None:
            raise ValueError('ورود کردن کد پرسنلی الزامی میباشد!')
        else:
            user = self.model(phone_number=phone_number, **extra_fields)
            user.password = make_password(password)
            user.save(using=self._db)
        
        return user
        
    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.") 
        
        return self.create_user(phone_number, password, **extra_fields)
    