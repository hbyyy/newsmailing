from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Keyword(models.Model):
    name = models.CharField(_('keyword name'), max_length=128)

    class Meta:
        db_table = 'keyword'

    def __str__(self):
        return self.name


class Subscription(models.Model):
    profile = models.ForeignKey('members.Profile',
                                on_delete=models.CASCADE)
    company = models.ForeignKey('articles.Company',
                                on_delete=models.CASCADE)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        db_table = 'subscription'
