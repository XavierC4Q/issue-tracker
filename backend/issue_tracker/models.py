import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """ User Manager that knows how to create users via email instead of username """

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()
    username = None
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', ]

    def __str__(self):
        return "{}".format(self.email)


class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  profile_id = models.AutoField(primary_key=True)
  fullname = models.CharField(blank=False, null=False, max_length=100)
  title = models.CharField(blank=True, null=True, max_length=100)

  REQUIRED_FIELDS = ['fullname', ]

  def __str__(self):
    return "Profile {}".format(self.user.email)
