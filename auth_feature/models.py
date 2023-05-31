from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import MyUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import random
import names
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.
class MyUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(_("email address"), unique=True)
    birthdate = models.DateField(_("Sinh nhật"), default= timezone.now() - timezone.timedelta(days=(3650-random.randint(100,1500))))
    gender = models.CharField(_("Giới tính"), max_length=1, choices=GENDER_CHOICES)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        default=names.get_full_name()
    )
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
