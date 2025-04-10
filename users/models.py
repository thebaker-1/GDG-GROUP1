from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)  # Hashed password
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)  # For soft deletion
    is_staff = models.BooleanField(default=False)  # Required for admin
    is_superuser = models.BooleanField(default=False)  # Required for admin
    date_joined = models.DateTimeField(default=now)

    following = models.ManyToManyField(
        'self',
        through='interactions.Follow',
        related_name='followers',
        symmetrical=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True