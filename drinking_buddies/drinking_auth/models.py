"""Authentication models."""

import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """Overwrites default django user manager."""

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates new User object.

        Args:
            username (str): user's username
            email (str): user's email
            password (str): user's password
            is_staff (bool): True if user is is part of service administration staff
            is_superuser (bool): True if user is superuser
        """

        if not email:
            raise ValueError("Users must have an email address")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        """
        Provides additional data to _create_user method.

        Args:
            username (str): user's username
            email (str): user's email
            password (str): user's password
        """

        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Creates superuser.

        Args:
            username (str): user's username
            email (str): user's email
            password (str): user's password
        """

        user = self._create_user(username, email, password, True, True, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Overwrites default django User model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=254, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [EMAIL_FIELD]

    objects = UserManager()

    def __repr__(self):
        return f"<User {self.username} id={self.id}>"
