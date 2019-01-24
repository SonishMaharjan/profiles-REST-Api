
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#base of django user model
from django.contrib.auth.models import AbstractBaseUser
#help to authenticate user :what they can do what they cant do
from django.contrib.auth.models import PermissionsMixin
#User profile manger
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps Django to work with customer user model."""

    def create_user(self,email,name,password=None):
        """"Creates new user profile object."""

        if not email:
            raise valueError("Users must have an email address.")

        #convert all emails to lower case ie standard form
        email = self.normalize_email(email)
        user = self.model(email=email, name = name)

        #encrytp password using hash
        user.set_password(password)

        user.save(using=self.db)

        return user;

    def create_superuser(self,email,name,password):
        """"create superuser with given details"""

        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)
        return user



# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """"Represents a 'user profile' inside our system  """
    email = models.EmailField(max_length=255,unique=True)

    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default =False)

    #object manager used to mange UserProfile like creating administrator user normal user authenticate
    objects = UserProfileManager()

    #django variable
    USERNAME_FIELD = 'email'

    #email is already REQUIRED_FIELDS cuz its USERNAME_FIELD
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ used to get full name """
        return self.name


    def get_short_name(self):
        """Used to get a user short name"""
        return self.name

    def __str__(self):
        """Djngo uses this to convert this object to string"""
        return email

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now= True)

    def __str__(self):
        """Return models as string"""
        return self.status_text
