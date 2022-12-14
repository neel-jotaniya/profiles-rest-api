from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user frofile"""
    def create_user(self,email,name,password = None):
        if not email :
            raise ValueError ("User must have email adress")
        email = self.normalize_email(email)
        user = self.model(email = email,name = name)
        
        user.set_password(password)
        user.save(using = self._db)
        
        return user
    
    def create_super_user(self,name,email,password):
        user = self.create_user(email,name,password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Database model for users in system"""
    
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    object = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    user = UserProfileManager()
    def get_full_name(self):
        return self.name
    
    def get_sort_name(self):
        return self.name
    
    def __str__(self) :
        return self.email
    
