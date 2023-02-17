from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy, reverse

class UserManager(BaseUserManager):
    '''User manager with no username but email.'''
    use_in_migrations = True

    def _create_user(self, email, password, role, **kwargs):
        if not email:
            raise ValueError('Email is a required field')
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, email, password = None, role=1, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, role, **kwargs)
    def create_superuser(self, email, password, role=1, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, role, **kwargs)


class User(AbstractUser):
    NORMAL = 3
    ADMIN = 2
    SUPERADMIN = 1
    USER_TYPE = (
        (NORMAL, _('Normal User')),
        (ADMIN, _('Admin User')),
        (SUPERADMIN, _('Super Admin User')),
    )
    role = models.PositiveSmallIntegerField(_('user_type'), choices=USER_TYPE, default=NORMAL)
    username = None
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self) -> str:
        return self.email