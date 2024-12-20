from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.managers import AppUserManager


# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    username = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'  # USERNAME_FIELD means the first credential in our auth
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    about_me = models.CharField(
        null=True,
        blank=True,
        max_length=500,
    )

    phone_number = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    occupation = models.CharField(
        null=True,
        blank=True,
        max_length=100,
    )