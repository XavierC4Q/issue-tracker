import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from .managers import UserManager


class User(AbstractUser):
    objects = UserManager()
    username = None
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', ]

    def __str__(self):
        return "User %s" % self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_id = models.AutoField(primary_key=True)
    fullname = models.CharField(blank=False, null=False, max_length=100)
    title = models.CharField(blank=True, null=True, max_length=100)

    REQUIRED_FIELDS = ['fullname', ]

    def __str__(self):
        return "Profile for %s" % self.user.email


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, unique=True, null=False)
    profiles = models.ManyToManyField(Profile)
    description = models.TextField(default='', max_length=1000)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    REQUIRED_FIELDS = ['name', 'profiles', ]

    def __str__(self):
        return "Team %s" % self.name
