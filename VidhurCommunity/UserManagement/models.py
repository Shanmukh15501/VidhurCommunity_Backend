from typing import Union

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

GenderChoice = (
        ( 0, 'Male'),
        ( 1, 'Fe-Male'),
        ( 2, 'Other'),
    )

class CustomUserManager(BaseUserManager):



    def create_user(self, email: str, password: str, **extra_fields) -> object:
        if not email:
            raise ValueError("Please Enter Email")
        if not password or len(password) < 3:
            raise ValueError("Please Enter Password with Valid Length")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email: str, password: str, **extra_fields) -> object:
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    
    def active_users(self):
        """
        Returns a queryset containing active users.
        """
        return self.get_queryset().filter(is_active=True)





class Users(AbstractUser, PermissionsMixin):

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        )
    )
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    phone = models.CharField(max_length=20, null=True,blank=True)
    gender = models.SmallIntegerField(choices=GenderChoice, null=True, blank=False, default=0, )
    is_staff = models.BooleanField(
        default=False,
        help_text=_("Designates whether the user can log into this admin site.")
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_phone_verified = models.BooleanField(
        default=False,
        help_text=_("Designates whether otp is validated while user creation.")
    )
    is_email_verified = models.BooleanField(
        default=False,
        help_text=_("Designates whether Email is validated while user creation.")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # If username is not set or empty, set it to the email value
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
    
    def get_tokens_for_user(self):

        token = RefreshToken.for_user(self)

        return {
                    'refresh': str(token),
                    'access': str(token.access_token),
               }

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
