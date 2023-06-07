from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from user.manager import CustomUserManager



class User(AbstractUser):
    username = models.CharField(max_length=225, unique=True, blank=True, null=True)
    full_name = models.CharField(_("Full Name"), max_length=50)
    phone_number = models.CharField(_("Phone Number"), max_length=50)
    email = models.EmailField(_('Email Address'), unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
      return "{}".format(self.email)
    