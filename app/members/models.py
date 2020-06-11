import uuid
from datetime import timedelta

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
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

    def expired(self, **kwargs):
        return self.filter(is_superuser=False, is_active=False, created__lte=timezone.now() - timedelta(days=3))


class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), max_length=128, unique=True)
    password = models.CharField(_('password'), max_length=128)
    created = models.DateTimeField(_('created date'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    token = models.UUIDField(_('activate token'), default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'user'
        indexes = [
            models.Index(fields=['is_active', 'id'], name='activate_index')
        ]

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


class Profile(models.Model):
    user = models.OneToOneField('members.User',
                                verbose_name=_('user'),
                                related_name='profile',
                                on_delete=models.CASCADE)
    keywords = models.ManyToManyField('members.Keyword',
                                      verbose_name=_('keyword'),
                                      related_name='profiles',
                                      db_table='subscribe')

    class Meta:
        db_table = 'profile'


class Keyword(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'keyword'

    def __str__(self):
        return self.name
