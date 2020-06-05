from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email):
        user = User.objects.create(email=self.normalize_email(email))
        user.set_password(self.make_random_password())
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email)
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(_('email'), max_length=128, unique=True)
    password = models.CharField(_('password'), max_length=128)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        db_table = 'members'

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser
