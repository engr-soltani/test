from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .custom_user_manager_model import CustomUserManager

# Create your models here.

class User(AbstractUser):
    username = models.CharField('User Name',max_length=32, unique=True,error_messages={'unique':"A user with that username already exists."})
    email = models.EmailField('Email',unique=True)
    first_name = models.CharField('First Name',max_length=30,blank=True)
    last_name = models.CharField('Last Name',max_length=30,blank=True)

    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as active. '
                                                'Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    last_seen = models.DateTimeField('last seen date', null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email