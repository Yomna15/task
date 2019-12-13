from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model


# User = get_user_model()
class UserManager(BaseUserManager):
    def create(self, email, password=None, **kyargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length = 255, null = False, unique = True)
    name = models.CharField(max_length = 255, null = True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, null = True)
    is_staff = models.BooleanField(default=False, null = True)
    is_superuser = models.BooleanField(default=False, null = True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

